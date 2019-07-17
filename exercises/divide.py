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
    FloatField,
    BooleanField,
    validators
)
from random import randint

from index import error


divide_blueprint = Blueprint('divide', __name__)
logger = logging.getLogger('divide')


class DivideForm(FlaskForm):
    """ Divide data FlaskForm

    :param FlaskForm:
    """
    p1 = FloatField('p1', [validators.DataRequired()])
    p2 = FloatField('p2', [validators.DataRequired()])
    result = FloatField('result', [validators.DataRequired()])
    correct = BooleanField('correct')
    submit = SubmitField('Check')


@divide_blueprint.route('/divide', methods=['GET', 'POST'])
@lti(request='session', error=error, app=app)
def index(lti=lti):
    """ initial access page for lti consumer

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    form = DivideForm()
    form.p1.data = float(randint(1, 9))
    form.p2.data = float(randint(1, 9))
    return render_template('divide/index.html', form=form)


@divide_blueprint.route('/divide/grade', methods=['POST'])
@lti(request='session', error=error, app=app)
def grade(lti=lti):
    """ post grade

    :param lti: the `lti` object from `pylti`
    :return: grade rendered by grade.html template
    """
    form = DivideForm(request.form)
    if not form.validate():
        return error(message='The divide form could not be validated.')

    correct = (round((form.p1.data / form.p2.data), 2) == form.result.data)
    form.correct.data = correct
    lti.post_grade(1 if correct else 0)
    return render_template('divide/grade.html', form=form)
