# Sample LTI Provider for Flask
This is a fork of [mitodl/mit_lti_flask_sample](https://github.com/mitodl/mit_lti_flask_sample).

## Intention:
With this pull request, multiple LTI providers are to be served with one flask application.

## Problem:
In order to be able to run multiple LTI providers from one flask application, it is necessary to store the LTI properties of the different LTI providers independently of the flask session. If the LTI properties of an LTI provider are saved in the flask session, they will be overwritten by their LTI properties when using another LTI provider.

## Solution:
The LTI properties are stored as LTI session objects in a database. Only the `user_id` is stored in the flask session. The assignment of a flask request to the LTI session object happens via the flask session's `user_id` and the request url path (`https://<host>:<port>/<path>`).

For this, the [pylti/flask.py](https://github.com/mitodl/pylti/blob/master/pylti/flask.py) ​​decorator had to be modified accordingly ([pyltiflask.py](https://github.com/openHPI/mit_lti_flask_sample/blob/master/pyltiflask.py)). This modification uses the configuration of the flask application and has therefore been integrated into the flask application.

## Example flask application:
This example flask application implements 3 simple LTI providers (add, multiply, divide). The initial LTI session (per LTI provider) is created by a request to the index controller. For an initial request, the custom parameter `custom_exercise` must be passed in addition to the default LTI properties. All subsequent requests to the LTI providers must have the LTI provider's name in the path. e.g. `http://localhost:5000/add`.

The example flask application provides another LTI provider for staff usage. The staff index controller only provides one route to view the LTI sessions.

## Install and run flask application:
This example flask application uses [Pipenv](https://github.com/pypa/pipenv) as package und virtualenv manager. sqlite3 is used here as database and [orator](https://orator-orm.com) as ORM.

```
# Clone Repository
git clone https://github.com/openHPI/mit_lti_flask_sample.git
cd mit_lti_flask_sample

# install packages virtualenv
pipenv install

# change into virtualenv (not necessary directly after pipenv install)
pipenv shell

# create and migrate database
orator migrate --force -c config.py

# run web
python openhpi_lti_flask_sample.py
```

## Usage
Do a request to `http://localhost:5000/` with the parameters like
```
oauth_consumer_key: __consumer_key__
oauth_signature_method: HMAC-SHA1
oauth_timestamp: 1563363262
oauth_nonce: eetk314j0F8MkpgL8j1GHtG6hf4cyHYJrR7zExQ
oauth_version: 1.0
context_id: 6a0c9b09-c873-4d49-8a51-c76aabf40bb4
context_title: Email-Excercise-LTI Testkurs
custom_exercise: add
launch_presentation_return_url: https://staging.openhpi.de/courses/testkurs2019/items/8L09GkGrjFETx5YGk5FPC/tool_return
lis_outcome_service_url: https://staging.openhpi.de/courses/testkurs2019/items/8L09GkGrjFETx5YGk5FPC/tool_grading
lis_person_contact_email_primary: matthias.wiesner@hpi.de
lis_person_name_family: Ymous
lis_person_name_full: Matthias Wiesner
lis_person_name_given: Anon
lis_result_sourcedid: 37802e8e-cd21-436c-96f3-42b705790be6
lti_message_type: basic-lti-launch-request
lti_version: LTI-1p0
resource_link_id: 517e43e4-384d-41c7-b2e7-33d1b88f0469
roles: Administrator
user_id: 4e8f71c9-942d-4c93-a6fa-0cdc2866fdaf
oauth_signature: NMGlOxZpYA4D0nvDe/F4AHpMXDg=
```
The parameters are mostly LTI standard, besides of `custom_exercise` which is mandatory to redirect to the accondingly LTI-Provider.

The request is redirected to `http://localhost:5000/add`. You can solve the addition; you are redirected to `http://localhost:5000/add/grade`.
Keep all browser tabs open (to keep the flask session alive) and do another request but with another `custom_exercise` (divide, multiply).