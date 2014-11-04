.. _Pylti architecture: https://github.com/mitodl/pylti/docs/_build/architecture.html
.. _mit lti flask sample template: https://github.mit.edu/mitxlti/mit_lti_flask_sample/
.. _deploy to heroku: deploy_to_heroku.rst

Tutorial: LTI interfacing to edX
================================

The mit_lti_flask_sample is a template for building LTI modules for edX.
The intent of this tutorial is to show how to:

    * Create a new LTI project from the sample template
    * deploy the sample
    * create an LTI from the sample
    * use the LTI in a course

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

Create a new LTI project from the sample template
*************************************************

In a browser go to `mit lti flask sample template`_ and copy the "SSH clone URL".
You will paste "SSH clone URL" in the "git clone" command below.

You will need to have an ssh keys for github, so here is a precise guide to
generating keys:

    https://help.github.com/articles/generating-ssh-keys/

In a terminal window execute the following commands (you may want to use sudo)::

    $ git clone --origin source SSH_clone_URL your-new-lti-project
    $ cd your-new-lti-project
    $ git create your-new-lti-project
    $ git log

Deploy the sample
*****************

.. toctree::

    deploy_to_heroku.rst

Create an LTI from the sample
*****************************

// a portion of creating LTI is in edX doc - look in HipChat from Peter to me
http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/lti_component.html

Use the LTI in a course
***********************

http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/lti_component.html

