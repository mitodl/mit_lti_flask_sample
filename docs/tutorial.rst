.. _mit lti flask sample template: https://github.mit.edu/mitxlti/mit_lti_flask_sample/
.. _deploy to heroku: deploy_to_heroku.rst

Tutorial: LTI interfacing to edX
================================

The mit_lti_flask_sample is a template for building LTI modules for edX.
The intent of this tutorial is to show how to:

    * Create a Virtual Environment to explore the LTI sample
    * Explore the LTI sample template
    * Setup edX locally
    * Use the LTI sample on the local server in a course
    * Deploy the LTI sample to a heroku server
    * Use the LTI sample on the heroku server in a course

This is a sample LTI provider for the Flask framework.  It is a minimal
implementation that provides a starting point for a custom LTI provider.
It is one of a series of LTI providers written for popular frameworks and
using the Python LTI library, PyLTI.  Additional sample LTI providers for
other Python frameworks are listed on the PyLTI GitHub site,
`https://github.com/mitodl/pylti
<https://github.com/mitodl/pylti>`_.  While these LTI provider examples can
be used with any LTI consumer, they were created for use with edX.  Integrating
an LTI provider with edX is described in the edX LTI `docs.
<http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/lti_component.html>`_

You will need both this app and the PyLTI library to create your own LTI
provider.  Each sample contains only the code variations necessary to support
its specific framework.  By creating an interface boundary between a sample
provider and PyLTI, PyLTI manages the specific LTI features and each sample
manages the specific requirements of its framework.  You can easily switch your
custom provider from one framework to another.

Please see the PyLTI README `https://github.com/mitodl/pylti
<https://github.com/mitodl/pylti>`_ for a detailed description of the architecture.

Create a Virtual Environment to explore the LTI sample
------------------------------------------------------

"A Virtual Environment ... is an isolated working copy of Python which allows
you to work on a specific project without worry of affecting other project."

Reference: `http://docs.python-guide.org/en/latest/dev/vertualenvs/ <http://docs.python-guide.org/en/latest/dev/vertualenvs/>`_

This sample expects the ``PyVENV`` folder to contain the Virtual Environment for the sample.

To ``CREATE`` the PyVENV Virtual Environment::

    $ cd ~
    $ pip install virtualenv
    $ virtualenv PyVENV

To ``ACTIVATE`` it::

    $ source ~/PyVENV/bin/activate

To ``DEACTIVATE`` it::

    (PyVENV) $ deactivate

To ``DESTROY`` it::

    (PyVENV) $ deactivate
    $ rm -Rv ~/PyVENV

Explore the LTI sample template
-------------------------------

You will need to have an ssh keys for GitHub, so here is a precise guide to
generating keys:

    https://help.github.com/articles/generating-ssh-keys/

In a terminal window execute the following commands::

    $ source ~/PyVENV/bin/activate
    $ mkdir my_Projects
    $ cd my_Projects
    $ git clone git@github.com/mitodl/mit_lti_flask_sample.git

To run the sample as http locally from my_Projects/mit_lti_flask_sample/::

    $ cd ~/my_Projects/mit_lti_flask_sample
    $ pip install -r requirements.txt (this may take a while)
    $ python mit_lti_flask_sample.py

    In a browser for running http type:

        http://127.0.0.1:5000/is_up

        If you see a page containing the words, "I'm up", you have verified that you can run the sample app locally.

To run the sample as https locally from my_Projects/mit_lti_flask_sample/::

    $ cd ~/my_Projects/mit_lti_flask_sample
    $ pip install -r requirements.txt (this may take a while)
    $ uwsgi --wsgi-file `pwd`/mit_lti_flask_sample.py --master --http 0.0.0.0:8400 --https 0.0.0.0:8443,scripts/foobar.crt,scripts/foobar.key --plugin python --py-autoreload 1 --honour-stdin --catch-exceptions --callable app

    In a browser for running https type:

        https://0.0.0.0:8443/is_up

        If you see a page containing the words, "I'm up", you have verified that you can run the sample app locally.


Setup edX locally
-----------------

The following section illustrates the steps for setting up and edX server
Other LTI consumers will have a similar process.

.. toctree::

    setup_edX_fullstack.rst


Use the LTI sample on the local server in a course
--------------------------------------------------

The following section illustrates the steps for creating and edX course to use the LTI sample.
Other LTI consumers will have a similar process.

Reference: `http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/lti_component.html <http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/lti_component.html>`_

In edX Studio you will use the LTI Sample in a new course.

    On the My Courses page  click the ``+ New Course`` button.
    In the Create a New Course form fill out the fields.

    Click on ``Settings->Advanced Setting``
    In Manual Policy Definition add the following:
        ======================= ========================
        Keys                    Values
        ======================= ========================
        Advanced Module List    ``[ "lti" ]``
        ----------------------- ------------------------
        LTI Passports           ``[ "lti_starx_add_demo:__consumer_key__:__lti_secret__" ]``
        ======================= ========================
    Click ``Save Changes``

    Click the ``+ New Section`` button and edit the Subsection to read ``Section LTI local``.

    Click the ``+ New Subsection`` button and enter "LTI Problem"
    Click the ``+ New Unit`` button
    Click the ``Advanced`` button
    Select LTI
    Edit the LTI problem and add:
        ======================= ========================
        Keys                    Values
        ======================= ========================
        LTI ID                  ``"lti_starx_add_demo:__consumer_key__:__lti_secret__"``
        ----------------------- ------------------------
        LTI URL                 ``http://127.0.0.1:5000/``
        ======================= ========================
    Click on ``"Save"``

    Click on ``"Publish"``
    Click on ``"Review Changes"``

    Verify that the LTI sample works:
        Displays the LTI user interface in the new problem
        Returns a grade


Deploy the LTI sample to a heroku server
----------------------------------------

Deploy the sample app to a server accessible from your LTI consumer (e.g edX or
another LMS).

If there is no server currently available from your LTI consumer.
The following instructions show how to deploy the sample to the
Heroku service, but the instructions are similar for any server.

.. toctree::

    deploy_to_heroku.rst

Use the LTI sample on the heroku server in a course
---------------------------------------------------

Run the LTI sample with http and https on the heroku server in a
browser as you did locally only with the heroku URLs (see above).

    Create a new problem that uses the LTI Sample
        Create a new problem of type ``Advanced->LTI``
        Edit the problem and you get a long form
            use passport thing
            use heroku server
        PUBLISH THE PROBLEM
        PREVIEW

    Verify that the LTI sample works:
        Displays the LTI user interface in the new problem
        Returns a grade

