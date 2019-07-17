import logging

from flask import (
    Blueprint,
    current_app as app,
    redirect,
    render_template,
    request,
    session,
    url_for)
from flask_wtf import FlaskForm
from pyltiflask import lti
from wtforms import (
    SubmitField,
    IntegerField,
    BooleanField,
    validators
)
from random import randint

from index import error


multiply_blueprint = Blueprint('multiply', __name__)
logger = logging.getLogger('multiply')


class MultiplyForm(FlaskForm):
    """ Multiply data FlaskForm

    :param FlaskForm:
    """
    p1 = IntegerField('p1', [validators.DataRequired()])
    p2 = IntegerField('p2', [validators.DataRequired()])
    result = IntegerField('result', [validators.DataRequired()])
    correct = BooleanField('correct')
    submit = SubmitField('Check')


@multiply_blueprint.route('/multiply', methods=['GET', 'POST'])
@lti(request='session', error=error, app=app)
def index(lti=lti):
    """ initial access page for lti consumer

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    form = MultiplyForm()
    form.p1.data = randint(1, 9)
    form.p2.data = randint(1, 9)
    return render_template('multiply/index.html', form=form)


@multiply_blueprint.route('/multiply/grade', methods=['POST'])
@lti(request='session', error=error, app=app)
def grade(lti=lti):
    """ post grade

    :param lti: the `lti` object from `pylti`
    :return: grade rendered by grade.html template
    """
    form = MultiplyForm(request.form)
    if not form.validate():
        return error(message='The multiply form could not be validated.')

    correct = ((form.p1.data * form.p2.data) == form.result.data)
    form.correct.data = correct
    lti.post_grade(1 if correct else 0)
    return render_template('multiply/grade.html', form=form)
