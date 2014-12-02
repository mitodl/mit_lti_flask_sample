.. _deploy to heroku: deploy_to_heroku.rst

Tutorial: Using the Sample LTI provider in edX
==============================================

The mit_lti_flask_sample is a Flask LTI provider template for edX.

The intent of this tutorial is to show how to:

    * Create a Virtual Environment to explore the sample LTI provider
    * Setup edX to run on localhost
    * Deploy the sample LTI provider locally
    * Use the local sample LTI provider in an edX course
    * Deploy the sample LTI provider to an heroku server
    * Use the heroku sample LTI provider in an edX course
    * Modifying the sample

This is a sample LTI provider for the Flask framework.  It is a minimal
implementation that provides a starting point for a custom LTI provider.
It is one of a series of LTI providers written for popular frameworks and
using the Python LTI library, PyLTI.  Additional sample LTI providers for
other Python frameworks are planned, see `https://github.com/mitodl/pylti
<https://github.com/mitodl/pylti>`_.  While these LTI provider examples can
be used with any LTI consumer, they were created for use with edX.  Integrating
an LTI provider with edX is described in the edX LTI `docs.
<http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/lti_component.html>`_

You will need both this app and the PyLTI library to create your own LTI
provider.  Each sample contains only the code variations necessary to support
its specific framework.  By creating an interface boundary between a sample
LTI provider and PyLTI, PyLTI manages the specific LTI features and each sample
manages the specific requirements of its framework.  You can easily switch your
custom provider from one framework to another.

Please see the PyLTI README `https://github.com/mitodl/pylti
<https://github.com/mitodl/pylti>`_ for a detailed description of the architecture.

Create a Virtual Environment to explore the sample LTI provider
---------------------------------------------------------------

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

Setup edX to run on localhost
-----------------------------

The following section illustrates the steps for setting up and edX server
Other LTI consumers will have a similar process.

.. toctree::

    setup_edX_fullstack.rst


Deploy the sample LTI provider locally
--------------------------------------

You will need to have an ssh keys for GitHub, so here is a precise guide to
generating keys:

    https://help.github.com/articles/generating-ssh-keys/

In a browser::

    Go to ``https://github.com/mitodl`` and fork the ``mit_lti_flask_sample`` repository
    to (say) ``https://github.com/my_repositories``.

    Navigate to the fork repository and change its name to (say) ``my_lti`` by:
        Clicking on ``Settings`` and changing the value of ``Repository name``.

In a terminal window execute the following commands::

    $ source ~/PyVENV/bin/activate
    $ mkdir my_Projects
    $ cd my_Projects
    $ git clone git@github.com/my_repositories/my_lti.git

To run the sample as http locally from my_Projects/my_lti/::

    $ cd ~/my_Projects/my_lti
    $ pip install -r requirements.txt (this may take a while)
    $ python my_lti.py

    In a browser for running http type:

        http://127.0.0.1:5000/is_up

        If you see a page containing the words, "I'm up", you have verified that you can run the sample app locally.

To run the sample as https locally from my_Projects/mit_lti_flask_sample/::

    $ cd ~/my_Projects/my_lti
    $ pip install -r requirements.txt (this may take a while)
    $ uwsgi --wsgi-file `pwd`/mit_lti_flask_sample.py --master --http 0.0.0.0:8400 --https 0.0.0.0:8443,certs/foobar.crt,certs/foobar.key --plugin python --py-autoreload 1 --honour-stdin --catch-exceptions --callable app

    In a browser for running https type:

        https://0.0.0.0:8443/is_up

        If you see a page containing the words, "I'm up", you have verified that you can run the sample app locally.


Use the local sample LTI provider in an edX course
--------------------------------------------------

The following section illustrates the steps for creating and edX course to use the sample LTI provider.
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

    For http - Edit the LTI problem and add:

        ======================= ========================
        Keys                    Values
        ======================= ========================
        LTI ID                  ``lti_starx_add_demo``
        ----------------------- ------------------------
        LTI URL                 ``http://127.0.0.1:5000``
        ----------------------- ------------------------
        Scored                  ``TRUE``
        ======================= ========================

    For https - Edit the LTI problem and add:

        ======================= ========================
        Keys                    Values
        ======================= ========================
        LTI ID                  ``lti_starx_add_demo``
        ----------------------- ------------------------
        LTI URL                 ``https://0.0.0.0:8443``
        ----------------------- ------------------------
        Scored                  ``TRUE``
        ======================= ========================

    Click on ``"Save"``

    Click on ``"Publish"``
    Click on ``"View Live Version"``

    Verify that the sample LTI provider works:
        Displays the LTI user interface in the new problem
        Returns a grade


Deploy the sample LTI provider to an heroku server
--------------------------------------------------

The following instructions show how to deploy the sample to the
Heroku service, but the instructions are similar for any server.

.. toctree::

    deploy_to_heroku.rst

Now that you have heroku installed and the sample deployed, it is useful to become familiar
with heroku terminal commands:

    Check that heroku is available::

        $ heroku (will print the heroku commands)

    Run the following general commands::

        $ heroku auth:whoami (will display either your Email or a login prompt)
        $ heroku auth:login (in case you are not already logged in)
        $ heroku auth:logout (and login again as a confidence building exercise)
        $ heroku apps (you should see your recently deployed app - if not, deploy your app)

    Once ``heroku apps`` shows your deployed app - let's assume it's name is sheltered-springs-4102,
    run the following commands on the app::

        $ heroku sharing --app sheltered-springs-4102 (this will show if you have collaborators)
        $ heroku addons --app sheltered-springs-4102 (this will show if you have addons)
        $ heroku config --app sheltered-springs-4102 (this will show if you have config variables)
        $ heroku domains --app sheltered-springs-4102 (this will show the name of your app's domain)
        $ heroku logs --app sheltered-springs-4102 (just in case)

    You need to add a DYNO process. The documentation lives in

        https://devcenter.heroku.com/articles/scaling

    Here are the commands::

        $ heroku ps:scale --app sheltered-springs-4102 web=1
        $ heroku ps --app sheltered-springs-4102 (this will show the current processes)


Use the heroku sample LTI provider in an edX course
---------------------------------------------------

    To use the heroku hosted sample LTI provider replace the LTI URL key from above:

    In a terminal window::

        $ heroku domains --app sheltered-springs-4102

    ``Note: sheltered-springs-41-2 is an example app. You created your app above. Use its name.``

    In the edX course LTI problem above:

        Click the ``Advanced`` button
        Select LTI

        For http - Edit the LTI problem and change ``127.0.0.1:5000`` to your app's domain name:

            ======================= ========================
            Keys                    Values
            ======================= ========================
            ----------------------- ------------------------
            ``LTI URL``             ``http://sheltered-springs-4102.herokuapp.com/``
            ----------------------- ------------------------
            ======================= ========================

Modifying the sample
--------------------

    The sample contains the following:

    ``my_lti``

        ``certs/``                      Needed for running sample LTI provider with https.
        ``docs/``                       LTI provider documentation as Shpinx restructured text.
        ``templates/``                  Sample LTI html used in mit_lti_flask_sample.py.
        ``.getignore``                  List of files that you don't want git to track.
        ``config.py``                   Configuration information needed for LTI sample provider.
        ``license.rst``                 The sample LTI provider license.
        ``mit_lti_flask_sample.py``     Key file for connecting the LTI to the edX.
        ``Procfile``                    Kicks off the mit_lti_flask_sample server.
        ``README.rst``                  Synopsis of this folder.
        ``requirements.txt``            Used to load all the libraries use by the LTI provider.
        ``runtime.txt``                 Defines the version of the runtime.


    Here is the control flow from the edX course to the sample LTI Provider:

        Your browser will call the edX Course Problem ``LTI URL`` (e.g.http://sheltered-springs-4102.herokuapp.com/)
        and server will execute sample Flask LTI Provider ``app`` (e.g. ``mit_lti_flask_sample``).

        The Flask app (see first few lines of ``mit_lti_flask_sample``) defines the following routes:

            ``@app.route('/',methods=['GET','POST'])``
            ``@app.route('/index', methods=['GET'])``
            ``@app.route('/lti/', methods=['GET','POST'])``

        Then executes the initial lti request:

            ``@lti(request='initial', error=error, app=app)``

            on @lti FAIL the following is executed:
                def error(exception=None)
                return render_template('error.html')

            on @lti OK the following is executed:
                def index(lti=lti)
                return render_template('index.html', lti=lti)

    For the Flask tutorial used in the creation this sample LTI provider see:

        http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
