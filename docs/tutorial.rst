.. _Pylti architecture: https://github.com/mitodl/pylti/docs/_build/architecture.html
.. _mit lti flask sample template: https://github.mit.edu/mitxlti/mit_lti_flask_sample/
.. _deploy to heroku: deploy_to_heroku.rst

Tutorial: LTI interfacing to edX
================================

The mit_lti_flask_sample is a template for building LTI modules for edX.
The intent of this tutorial is to show how to:

    * Create a Virtual Environment to explore the LTI sample
    * Explore the LTI sample template
    * Create a new LTI project from the sample template
    * Deploy the sample
    * Create an LTI from the sample
    * Use the LTI in a course

This is a sample LTI provider for the Flask framework.  It is one of a series of
LTI providers written for popular frameworks.  Each of these samples consumes
the pylti module.  You will need both this app and the pylti module to run
the sample.

By creating an interface boundary between the provider and
the library, each sample contains only the code variations necessary to support
its specific framework.  Since the interface to the pylti module remains the
same for each, you may easily switch your custom provider from one framework to
another.

For a description of the architecture please see `Pylti architecture`_.

Create a Virtual Environment to explore the sample
**************************************************

"A Virtual Environment ... is an isolated working copy of Python which allows
you to work on a specific project without worry of affecting other project."

    http://docs.python-guide.org/en/latest/dev/vertualenvs/

This sample expects the ``PyVENV`` folder to contain the Virtual Environment.

To ``CREATE`` the PyVENV Virtual Environment::

    $ pip install virtualenv
    $ virtualenv PyVENV

To ``ACTIVATE`` it::

    $ source PyVENV/bin/activate

To ``DEACTIVATE`` it::

    (PyVENV) $ deactivate

To ``DESTROY`` it::

    (PyVENV) $ deactivate
    $ rm -Rv ./PyVENV

Explore the LTI sample template
*********************************

You will need to have an ssh keys for github, so here is a precise guide to
generating keys:

    https://help.github.com/articles/generating-ssh-keys/

.. warning::

    In the ``git clone`` line below:

        git@github.mit.edu:mitxlti/mit_lti_flask_sample.git expects the cloner to be a repository contributor.
        git@github.mit.edu:mitxlti/mit_lti_flask_sample.git needs to be replaced below with the production repository’s URL.

In a terminal window execute the following commands::

    $ mkdir my_Projects
    $ cd my_Projects
    $ git clone git@github.mit.edu:mitxlti/mit_lti_flask_sample.git mit_lti_flask_sample
    $ cd mit_lti_flask_sample
    $ pip install -r requirements.txt

The pip install may take a while.

To run the sample locally:

    $ ls mit_lti_flask_sample
    $ cd mit_lti_flask_sample
    $ python mit_lti_flask_sample.py

In a browser for running http type:

    http://127.0.0.1:5000/is_up

In a browser for running https type:

    uwsgi --wsgi-file `pwd`/mit_lti_flask_sample.py --master --http 0.0.0.0:8400 --https 0.0.0.0:8443,scripts/foobar.crt,scripts/foobar.key --plugin python --py-autoreload 1 --honour-stdin --catch-exceptions --callable app


Create a new LTI from the sample
*****************************

Make a new one::

    $ git clone --origin source SSH_clone_URL your-new-lti-project
    $ cd your-new-lti-project
    $ git create your-new-lti-project
    $ git log
    $ sudo pip install -r requirements.txt

// a portion of creating LTI is in edX doc - look in HipChat from Peter to me
http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/lti_component.html

Deploy the new LTI
******************

.. toctree::

    deploy_to_heroku.rst

Use the LTI in a course
***********************

http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/lti_component.html

