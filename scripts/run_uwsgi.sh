#!/bin/bash
uwsgi --wsgi-file `pwd`/mit_lti_flask_sample.py --master --http 0.0.0.0:8400 --virtualenv ~/PyVENV/mit_lti_flask_sample --https 0.0.0.0:8443,foobar.crt,foobar.key --plugin python --py-autoreload 1 --honour-stdin --catch-exceptions --pythonpath ../pylti --callable app
