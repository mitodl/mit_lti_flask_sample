Deploy to Heroku
================

Heroku is a popular hosting service that offers free deployment for low volume
applications and a sliding pricing model for higher demand applications.  For the
purpose of documentation, we will use use Heroku as our deployment target though
you may deploy to most any host you want.

Application changes for Heroku Support
--------------------------------------

The items described below are in the sample solely to support Heroku deployment.
If you are not deploying to Heroku, you can ignore them.

Procfile
************

Heroku requires a text file named ``Procfile`` to reside in the application's root
directory.  Heroku documents the contents of the Procfile
`here. <https://devcenter.heroku.com/articles/procfile>`_

runtime.txt
***********

Heroku uses the contents of ``runtime.txt`` to pin the Python runtime to a specific
version.  The app has been tested with the Python runtime version found in the file.

Heroku Deployment
-----------------

The documentation provided by Heroku for preparing your machine and installing
required software is superb.  We could hardly improve on its clarity and detail.

Heroku 'getting started' tutorial
*********************************

Heroku 'getting started' tutorial contains these steps.

1. Introduction - Get a Heroku account and configure your machine
#. Set up - install the Heroku Toolbelt, upload your SSH keypair
#. Prepare the app - This step of the Heroku tutorial presumes you don't have an
   app to deploy, but you do!  In your terminal window, navigate to the file
   system directory that contains the sample application you cloned earlier.
#. Deploy the app



Get a Heroku account
***********************

#. Navigate to `https://www.heroku.com <https://www.heroku.com>`_ to sign up for a
free account.  If you already have an account, navigate to
`https://devcenter.heroku.com/articles/getting-started-with-python#introduction
<https://devcenter.heroku.com/articles/getting-started-with-python#introduction>`_
to proceed with the process.



Foreman development server
**************************

Heroku provides a development server called ``foreman`` as part of its "Heroku Toolbelt".
(You should have installed the "Toolbelt" as one of the steps to configure local
Heroku support.)  Foreman allows you to simulate the Heroku runtime environment
locally; very handy to help you verify that your app will run once deployed.  You
can run your app with this terminal command ``foreman start``.  Once your app starts,
navigate to ``http://localhost:5000/is_up`` to confirm that the app is working.  The
page will display the text "I'm up".



