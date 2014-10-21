#!/bin/bash

source ~/PyVENV/mit_lti_flask_sample/bin/activate
export PYTHONPATH=../pylti:$PYTHONPATH
python mit_lti_flask_sample.py
