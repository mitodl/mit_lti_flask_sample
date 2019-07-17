# -*- coding: utf-8 -*-
"""
    PyLTI decorator implementation for flask framework
"""
from __future__ import absolute_import
from functools import wraps
import logging

from flask import session, current_app, Flask
from flask import request as flask_request

from pylti.common import (
    LTI_SESSION_KEY,
    LTI_PROPERTY_LIST,
    verify_request_common,
    default_error,
    LTIException,
    LTINotInSessionException,
    LTIBase
)

from models import LtiSession

log = logging.getLogger('pylti.flask')  # pylint: disable=invalid-name

LTI_PROPERTIES = [
    'custom_exercise',
    LTI_SESSION_KEY
] + LTI_PROPERTY_LIST


class LTI(LTIBase):
    """
    LTI Object represents abstraction of current LTI session. It provides
    callback methods and methods that allow developer to inspect
    LTI basic-launch-request.

    This object is instantiated by @lti wrapper.
    """

    def __init__(self, lti_args, lti_kwargs):
        self.lti_session = self.get_ltisession()

        LTIBase.__init__(self, lti_args, lti_kwargs)
        # Set app to current_app if not specified
        if not self.lti_kwargs['app']:
            self.lti_kwargs['app'] = current_app

    def _consumers(self):
        """
        Gets consumer's map from app config

        :return: consumers map
        """
        app_config = self.lti_kwargs['app'].config
        config = app_config.get('PYLTI_CONFIG', dict())
        consumers = config.get('consumers', dict())
        return consumers

    def verify_request(self):
        """
        Verify LTI request
        :raises: LTIException is request validation failed
        """
        if flask_request.method == 'POST':
            params = flask_request.form.to_dict()
        else:
            params = flask_request.args.to_dict()
        log.debug(params)

        self.lti_session.delete()
        self.lti_session = self.get_ltisession(params=params)

        log.debug('verify_request?')
        try:
            verify_request_common(self._consumers(), flask_request.url,
                                  flask_request.method, flask_request.headers,
                                  params)
            log.debug('verify_request success')

            # All good to go, store all of the LTI params into a
            # session dict for use in views
            for prop in LTI_PROPERTIES:
                if params.get(prop, None):
                    log.debug("params %s=%s", prop, params[prop])
                    setattr(self.lti_session, prop, params[prop])

            session['user_id'] = params['user_id']

            # Set logged in session key
            setattr(self.lti_session, LTI_SESSION_KEY, True)
            self.lti_session.save()

            return True
        except LTIException:
            log.debug('verify_request failed')
            self.close_session()
            raise

    @property
    def response_url(self):
        """
        Returns remapped lis_outcome_service_url
        uses PYLTI_URL_FIX map to support edX dev-stack

        :return: remapped lis_outcome_service_url
        """
        url = self.lti_session.lis_outcome_service_url or ""
        app_config = self.lti_kwargs['app'].config
        urls = app_config.get('PYLTI_URL_FIX', dict())
        # url remapping is useful for using devstack
        # devstack reports httpS://localhost:8000/ and listens on HTTP
        for prefix, mapping in urls.items():
            if url.startswith(prefix):
                for _from, _to in mapping.items():
                    url = url.replace(_from, _to)
        return url

    def _verify_any(self):
        """
        Verify that an initial request has been made, or failing that, that
        the request is in the session
        :raises: LTIException
        """
        log.debug('verify_any enter')

        # Check to see if there is a new LTI launch request incoming
        newrequest = False
        if flask_request.method == 'POST':
            params = flask_request.form.to_dict()
            initiation = "basic-lti-launch-request"
            if params.get("lti_message_type", None) == initiation:
                newrequest = True
                # Scrub the session of the old authentication
                self.close_session()

        # Attempt the appropriate validation
        # Both of these methods raise LTIException as necessary
        if newrequest:
            self.verify_request()
        else:
            self._verify_session()

    def get_ltisession(self, params={}):
        """
        Get lti_session based on flask.path. Flask path must be the same
        as the exercise name
        Otherwise the lti_session is treated as initial request.

        current_app.config['EXERCISE_MAP'] MUST be defined
        """
        custom_exercise = None

        path = flask_request.path.split('/')[1].split('?')[0]
        for exercise in current_app.config['EXERCISE_MAP'].keys():
            if exercise == path:
                custom_exercise = exercise
                break
        else:
            # a new LTI launch request
            custom_exercise = params.get('custom_exercise', None)

        lti_session = LtiSession \
            .where('user_id', '=', session.get('user_id', None)) \
            .where('custom_exercise', '=', custom_exercise) \
            .first()

        if not lti_session:
            lti_session = LtiSession()

        self.session = lti_session
        return lti_session

    def _verify_session(self):
        """
        Verify that session was already created

        :raises: LTIException
        """
        def _fail():
            log.debug('verify_session failed')
            raise LTINotInSessionException('Session expired or unavailable')

        try:
            if not getattr(self.lti_session, LTI_SESSION_KEY):
                _fail()
        except AttributeError:
            _fail()

    def close_session(self):
        """
        Invalidates session
        """
        if session.get('user_id', None):
            del session['user_id']

        self.lti_session.delete()
        self.lti_session = self.get_ltisession()


def lti(app=None, request='any', error=default_error, role='any',
        *lti_args, **lti_kwargs):
    """
    LTI decorator

    :param: app - Flask App object (optional).
        :py:attr:`flask.current_app` is used if no object is passed in.
    :param: error - Callback if LTI throws exception (optional).
        :py:attr:`pylti.flask.default_error` is the default.
    :param: request - Request type from
        :py:attr:`pylti.common.LTI_REQUEST_TYPE`. (default: any)
    :param: roles - LTI Role (default: any)
    :return: wrapper
    """

    def _lti(function):
        """
        Inner LTI decorator

        :param: function:
        :return:
        """

        @wraps(function)
        def wrapper(*args, **kwargs):
            """
            Pass LTI reference to function or return error.
            """
            try:
                the_lti = LTI(lti_args, lti_kwargs)
                the_lti.verify()
                the_lti._check_role()  # pylint: disable=protected-access
                kwargs['lti'] = the_lti
                return function(*args, **kwargs)
            except LTIException as lti_exception:
                error = lti_kwargs.get('error')
                exception = dict()
                exception['exception'] = lti_exception
                exception['kwargs'] = kwargs
                exception['args'] = args
                return error(exception=exception)

        return wrapper

    lti_kwargs['request'] = request
    lti_kwargs['error'] = error
    lti_kwargs['role'] = role

    if (not app) or isinstance(app, Flask):
        lti_kwargs['app'] = app
        return _lti
    else:
        # We are wrapping without arguments
        lti_kwargs['app'] = None
        return _lti(app)
