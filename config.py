WTF_CSRF_ENABLED = True
""" enable CSRF
"""

SECRET_KEY = 'you-will-never-guess'
""" secret key for authentication
"""

PYLTI_CONFIG = {
    "consumers":{
        "__consumer_key__":{ "secret":"__lti_secret__"}
    }
}

PYLTI_URL_FIX = {
""" Remap URL to fix edX's misrepresentation of https protocol.
    You can add another dict entry if you have trouble with the
    PyLti URL.
"""

    "https://localhost:8000/": {
        "https://localhost:8000/": "http://localhost:8000/"
    },
    "https://localhost/": {
        "https://localhost/":"http://192.168.33.10/"
    }
}