from flask import Flask, session
from flask import render_template
from flask.ext.wtf import Form
from wtforms import IntegerField, BooleanField
from random import randint

from pylti.flask import lti

app = Flask(__name__)
app.config.from_object('config')


class AddFrom(Form):
    p1 = IntegerField('p1')
    p2 = IntegerField('p2')
    result = IntegerField('result')
    correct = BooleanField('correct')

@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/')
@app.route('/index', methods=['GET'])
@lti(request='any', error=error)
def hello_world(lti=lti):
    return render_template('index.html', lti=lti)


@app.route('/add', methods=['GET'])
@lti(request='session', error=error)
def add_form(lti=lti):
    form = AddFrom()
    form.p1.data = randint(1, 100)
    form.p2.data = randint(1, 100)
    return render_template('add.html', form=form)


@app.route('/grade', methods=['POST'])
@lti(request='session', error=error)
def grade(lti=lti):
    form = AddFrom()
    correct = ((form.p1.data + form.p2.data) == form.result.data)
    form.correct.data = correct
    lti.post_grade(1 if correct else 0)
    return render_template('grade.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
