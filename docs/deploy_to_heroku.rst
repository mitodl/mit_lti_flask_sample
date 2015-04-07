Deploy to Heroku
================
|Deploy|

.. |Deploy| image:: https://www.herokucdn.com/deploy/button.png
   :target: https://heroku.com/deploy

An LTI provider must run on a server accessible by your LTI consumer.  This
documentation assumes your LTI consumer is edX, but the principle is the same
for other LTI consumers.

Heroku is a popular hosting service that offers free deployment for low volume
applications and a sliding pricing model for higher demand applications.  For the
purpose of documentation we will use Heroku as our deployment target though
you may deploy to any host or hosting service you choose.

The following steps have these prerequisites:

* you have cloned the ``mit_lti_flask_sample`` to your development machine
* you can open a terminal window and navigate to the cloned sample code
* you have installed the ``git`` command line tool, or some other git client.

.. note::
   The following steps presume that you have a collection of command line
   utilities installed on your machine.  These utilities are installed by
   default on Linux machines, and freely available for OSX.  This link will
   guide you to resources for your operation system:
   :doc:`cmd_line_tools`

Heroku Deployment
-----------------

The documentation that Heroku provides for preparing your machine and installing
required software is excellent.  Start there by getting a Heroku account and
following the Python track of their tutorial.

1. Sign up for a free account by navigating to
   `https://www.heroku.com <https://www.heroku.com>`_.  If you already have an
   account, navigate to
   `https://devcenter.heroku.com/articles/getting-started-with-python#introduction
   <https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_
   to proceed with the Heroku tutorial.

#. Once you have an account, the Heroku site will guide you to install the Heroku
   Toolbelt and upload your SSH keypair.  Your SSH keypair authenticates you to
   Heroku.  If you don't have a SSH keypair, Heroku provides a link on that page
   to help you create one.

#. The next step of the Heroku tutorial, "Prepare the app", presumes you don't
   have an app to deploy, but you do.  Before continuing with the Heroku tutorial,
   let's first confirm that your app will run in the Heroku environment.  Do
   this by using an application installed as part of the Heroku Toolbelt.

#. In your terminal window, navigate to the file system directory that contains
   the sample application you cloned earlier.  If you haven't cloned the sample
   app to a local directory, see this guide :doc:`tutorial`.)

#. Heroku provides a development server called ``foreman`` as part of its
   "Heroku Toolbelt".  (You should have installed the "Toolbelt" in the
   'Introduction' step of the Heroku 'getting started' process.)  Foreman
   allows you to simulate the Heroku runtime environment locally; very handy
   to help you verify that your app will run once deployed.  You can run your
   app with this terminal command:

.. code-block:: bash

  foreman start

6. Once your app starts, navigate to
   ``http://localhost:5000/is_up`` to confirm that the app is working.  The
   page will display the text "I'm up" if the app is working properly.  To
   terminate the app, type ``Cntl-C`` in the terminal.

#. Now that you know that your app will run in the Heroku environment, your
   next step is to deploy your app to Heroku.  Proceed to the "Deploy the app"
   step in the Heroku tutorial.Use the ``create`` command to deploy your app:

.. code-block:: bash

  heroku create
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

Additional Heroku Configuration
-------------------------------

We recommend not storing secrets inside the git repository such as the
OAuth keys needed for LTI security.  As a result, we have instrumented
the ``config.py`` file to have an example of using environment
variables to store these secrets.

For example:

.. code-block:: python

  # secret key for authentication
  SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "you-will-never-guess")
  CONSUMER_KEY_PEM_FILE = os.path.abspath('consumer_key.pem')
  with open(CONSUMER_KEY_PEM_FILE, 'w') as wfile:
      wfile.write(os.environ.get('CONSUMER_KEY_CERT', ''))

  PYLTI_CONFIG = {
	  "consumers": {
		  "__consumer_key__": {
			  "secret": os.environ.get("CONSUMER_KEY_SECRET", "__lti_secret__"),
			  "cert": CONSUMER_KEY_PEM_FILE
		  }
	  }
  }

Now it is attempting to get the ``FLASK_SECRET_KEY``, the
``CONSUMER_KEY_CERT`` and ``CONSUMER_KEY_SECRET`` environment
variable values for the actual secrets.  To do this in Heroku you
can set these variables with the ``heroku config`` commands.  To set
the flask secret to ``pink_unicorns`` and ``__consumer_key__`` secret
to ``horn_of_plenty`` you would run:

.. code-block:: bash

  heroku config:set FLASK_SECRET_KEY=pink_unicorn CONSUMER_KEY_SECRET=horn_of_plenty

To check your configuration, you can run ``heroku config`` by itself,
and it will show what environment variables are set for your
application.

To replicate the secure configuration locally using ``foreman`` you can create a file in the root of the application at ``.env`` that contains K=V values for configuration.  i.e.

.. code-block:: bash

  FLASK_SECRET_KEY=pink_unicorn
  CONSUMER_KEY_SECRET=horn_of_plenty

.. note::

  Environment variables can be absolutely huge, so there is no problem
  storing full client SSL certificates in the
  ``CONSUMER_KEY_PEM_FILE`` if your application requires client
  certificates in addition to the OAuth scheme.  ``config.py`` above,
  for example, reads the environment variable the SSL certificate and
  key and writes it out to a file for use by ``httplib`` during
  execution on Heroku.

.. note::

  Developers whose LTI app will be consumed by MITx will need an application
  certificate issued by MIT IS&T to be able to send grades to edX.  You can
  request an application certificate by following the instructions at this
  support page
  `https://wikis.mit.edu/confluence/display/devtools/How+to+acquire+and+verify+a+x509+Application+Certificate
  <https://wikis.mit.edu/confluence/display/devtools/How+to+acquire+and+verify+a+x509+Application+Certificate>`_

Files added for Heroku Support
------------------------------

The items described below are in the sample solely to support Heroku deployment.
If you don't deploy to Heroku, you can ignore or remove them.

``Procfile``
^^^^^^^^^^^^

Heroku requires a text file named ``Procfile`` to reside in the application's
root directory.  Heroku documents the contents of the Procfile here:
`https://devcenter.heroku.com/articles/procfile
<https://devcenter.heroku.com/articles/procfile>`_

``runtime.txt``
^^^^^^^^^^^^^^^

Heroku uses the contents of ``runtime.txt`` to pin a specific version of the
Python runtime to a specific version.  The app has been tested with the Python
runtime version found in the file.



