from flask import Flask
from pylti.flask import lti

app = Flask(__name__)


@app.route('/')
@lti(request='any')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
