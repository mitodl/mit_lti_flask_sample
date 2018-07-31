# USAGE:
# $ docker build -t mit_lti_flask_sample .
# $ docker run -it --rm -p 5000:5000 --name lti-sample mit_lti_flask_sample

FROM python:2-onbuild

# to be accessible from outside the container, need to listen on all interfaces
ENV FLASK_LTI_HOST="0.0.0.0"

CMD [ "python", "./mit_lti_flask_sample.py" ]
