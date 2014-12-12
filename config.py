# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = 'you-will-never-guess'

PYLTI_CONFIG = {
    "consumers":{
        "__consumer_key__":{ "secret":"__lti_secret__"}
    }
}

# Remap URL to fix edX's misrepresentation of https protocol.
# You can add another dict entry if you have trouble with the
# PyLti URL.
PYLTI_URL_FIX = {
    "https://localhost:8000/": {
        "https://localhost:8000/": "http://localhost:8000/"
    },
    "https://localhost/": {
        "https://localhost/":"http://192.168.33.10/"
    }
}
