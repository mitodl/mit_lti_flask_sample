WTF_CSRF_ENABLED = True
"""
"""

SECRET_KEY = 'you-will-never-guess'
PYLTI_CONFIG = {
    "consumers":{
        "__consumer_key__":{ "secret":"__lti_secret__"}
    }
}

PYLTI_URL_FIX = {
    "https://localhost:8000/": {
        "https://localhost:8000/": "http://localhost:8000/"
    }
}