import logging

from flask import Blueprint
from flask import current_app as app
from flask import (
    redirect,
    render_template,
    request, url_for
)
from pyltiflask import lti

from models import LtiSession


logger = logging.getLogger('index_controller')

index_blueprint = Blueprint('index', __name__)


def error(exception=None, message=None):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('index/error.html', exception=exception, message=message)


@index_blueprint.route('/is_up', methods=['GET'])
def hello_world():
    """ Indicate the app is working. Provided for debugging purposes.

    :param lti: the `lti` object from `pylti`
    :return: simple page that indicates the request was processed by the lti
        provider
    """
    return render_template('index/up.html', lti=lti)


@index_blueprint.route('/staff', methods=['GET', 'POST'])
@lti(request='session', error=error, role='staff', app=app)
def staff(lti=lti):
    """ render the contents of the staff.html template

    :param lti: the `lti` object from `pylti`
    :return: the staff.html template rendered
    """
    sessions = LtiSession().all()
    return render_template('index/staff.html', lti=lti, sessions=sessions)


@index_blueprint.route('/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def index(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    Um zu den einzelnen Uebungen zu kommen, muss das Argument
    `custom_exercise` mitgegeben werden.

    :param lti: the `lti` object from `pylti`
    :return: lti page depending on param for lti provider
    """

    exercise = request.form.get('custom_exercise', None)
    logger.error('Exercise: %s', exercise)

    if exercise in app.config['EXERCISE_MAP']:
        # 307 = preserve http method
        return redirect(url_for(app.config['EXERCISE_MAP'][exercise]), code=307)
    else:
        return redirect(url_for('index.hello_world'))
