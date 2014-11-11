Deploy to Heroku
================

Heroku is a popular hosting service that offers free deployment for low volume
applications and a sliding pricing model for higher demand applications.

Application changes for Heroku Support
--------------------------------------

The items described below support Heroku deployment.

procfile
************

Heroku requires a text file named ``Procfile`` to reside in the application's root
directory.  Heroku documents the contents of the Procfile
`here. <https://devcenter.heroku.com/articles/procfile>`_

runtime.txt
***********

Heroku uses the contents of ``runtime.txt`` to pin the Python runtime to a specific
version.  The app has been tested with the Python runtime version found in the file.

Foreman development server
**************************

Heroku provides a development server called ``foreman`` as part of its "Heroku Toolbelt".
(You should have installed the "Toolbelt" as one of the steps to configure local
Heroku support.)  Foreman allows you to simulate the Heroku runtime environment
locally; very handy to help you verify that your app will run once deployed.  You
can run your app with this terminal command ``foreman start``.  Once your app starts,
navigate to ``http://localhost:5000/is_up`` to confirm that the app is working.  The
page will display the text "I'm up".  (You were hoping for something more flashy?)



