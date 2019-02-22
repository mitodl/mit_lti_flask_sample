"""
Configuration file for flask sample application
"""
import os


# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "you-will-never-guess")

# Sample client certificate example for 12 factor app
# You would want to store your entire pem in an environment variable
# with something like:
# ```
# export CONSUMER_KEY_CERT=$(cat <<EOF
# < paste cert here>
# EOF
# )
# ```

# The following would be the PYLTI_CONFIG for including a CONSUMER_KEY_PEM_FILE
# This is NOT needed by default
# CONSUMER_KEY_PEM_FILE = os.path.abspath('consumer_key.pem')
# with open(CONSUMER_KEY_PEM_FILE, 'w') as wfile:
#     wfile.write(os.environ.get('CONSUMER_KEY_CERT', ''))

# PYLTI_CONFIG = {
#     "consumers": {
#         "__consumer_key__": {
#             "secret": os.environ.get("CONSUMER_KEY_SECRET", "__lti_secret__"),
#             "cert": CONSUMER_KEY_PEM_FILE
#         }
#     }
# }

# The following would be the PYLTI_CONFIG for a generic consumer.
# The value of __consumer_key__ can be updated, but it will be the value of the client key 
PYLTI_CONFIG = {
    "consumers": {
        "__consumer_key__": {
            "secret": os.environ.get("CONSUMER_KEY_SECRET", "__lti_secret__")
        }
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
        "https://localhost/": "http://192.168.33.10/"
    }
}
