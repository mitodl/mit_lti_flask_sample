Deploy to Heroku
================

An LTI provider must run on a server accessible by your LTI consumer.  This
documentation assumes your LTI consumer is edX, but the principle is the same
for other LTI consumers.

Heroku is a popular hosting service that offers free deployment for low volume
applications and a sliding pricing model for higher demand applications.  For the
purpose of documentation we will use use Heroku as our deployment target though
you may deploy to any host or hosting service you choose.

The following steps have these prerequisites:

* you have cloned the ``mit_lti_flask_sample`` to your development machine
* you can open a terminal window and navigate to the cloned sample code
* you have installed the ``git`` command line tool, or some other git client.

.. note::

   The following steps presume that you have a collection of command line
   utilities installed on your machine.  These utilities are installed by
   default on Linux machines, and freely available for OSX.  This link will
   guide you to resources for your operation system: :doc:`cmd_line_tools`

Heroku Deployment
-----------------

The documentation that Heroku provides for preparing your machine and installing
required software is excellent.  Start there by getting a Heroku account and
following the Python track of their tutorial.

1. In your browser, navigate to `https://www.heroku.com <https://www.heroku.com>`_
   to sign up for a free account.
#. Once you have an account, the Heroku site will guide you to install the Heroku
   Toolbelt and upload your SSH keypair.  Your SSH keypair authenticates you to
   Heroku.  If you don't have a SSH keypair, Heroku provides a link on their page
   to help you create one.
#. The next step of the Heroku tutorial, "Prepare the app", presumes you don't
   have an app to deploy, but you do!  (If you haven't cloned the sample app to
   a local directory, see this guide. **!!Add link to git clone Tutorial!!**)
   In your terminal window, navigate to the file system directory that contains
   the sample application you cloned earlier and proceed to the "Deploy the app"
   step in the Heroku tutorial.

Before continuing with the Heroku deployment, let's first confirm that your app
will run in the Heroku environment.  You can do this by using an application
installed as part of the Heroku Toolbelt.

``foreman`` development server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heroku provides a development server called ``foreman`` as part of its "Heroku
Toolbelt".  (You should have installed the "Toolbelt" in the 'Introduction'
step of the Heroku 'getting started' process.)  Foreman allows you to simulate
the Heroku runtime environment locally; very handy to help you verify that
your app will run once deployed.  You can run your app with this terminal
command: ::

  $ foreman start

Once your app starts, navigate to
``http://localhost:5000/is_up`` to confirm that the app is working.  The
page will display the text "I'm up" if the app is working properly.  To
terminate the app, type ``Cntl-C`` in the terminal.

Now that you know that your app will run in the Heroku environment, your next
step is to deploy your app to Heroku.  Use the ``create`` is command to deploy
your app: ::

  $ heroku create
  Creating salty-tundra-1591... done, stack is cedar-14
  https://salty-tundra-1591.herokuapp.com/ | git@heroku.com:salty-tundra-1591.git

The ``create`` command returns useful information.  It indicates

* success or failure,
* the Heroku platform stack that your app runs in,
* the URL for your deployed app on Heroku
  (In this case, https://salty-tundra-1591.herokuapp.com/)
* the Git URL for your Git repository on Heroku
  (In this case, git@heroku.com:salty-tundra-1591.git)

You can now use the URL of your deployed app on Heroku to test the sample
against your edX course.

Application changes made for Heroku Support
-------------------------------------------

The items described below are in the sample solely to support Heroku deployment.
If you are not deploying to Heroku, you can ignore or remove them.

``Procfile``
^^^^^^^^^^^^

Heroku requires a text file named ``Procfile`` to reside in the application's root
directory.  Heroku documents the contents of the Procfile here:
`https://devcenter.heroku.com/articles/procfile
<https://devcenter.heroku.com/articles/procfile>`_

``runtime.txt``
^^^^^^^^^^^^^^^

Heroku uses the contents of ``runtime.txt`` to pin the Python runtime to a specific
version.  The app has been tested with the Python runtime version found in the file.


----

Parking lot for snippits
------------------------

If you already have an account, navigate to
`https://devcenter.heroku.com/articles/getting-started-with-python#introduction
<https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_
to proceed with the process.

Get a Heroku account
^^^^^^^^^^^^^^^^^^^^

Heroku 'getting started' tutorial contains these steps.

1. Introduction - Get a Heroku account and configure your machine
#. Set up - install the Heroku Toolbelt, upload your SSH keypair

