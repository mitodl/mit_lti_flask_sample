Sample LTI Provider for Flask
=============================

This is a sample LTI provider for the Flask framework [#f1]_.  It is a minimal
implementation that provides a starting point for a custom LTI provider.
It is one of a series of LTI providers written for popular frameworks and
using the Python LTI library, PyLTI.  Additional sample LTI providers for
other Python frameworks are planned.  Check for them on the PyLTI Github site,
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

Quick Start
-----------

1. Clone this repository,
   ``git clone git@github.mit.edu:mitxlti/mit_lti_flask_sample.git``
   and navigate to its directory
#. Run ``pip install -r requirements.txt``
#. Run ``scripts/run.sh``
#. Navigate to ``http://localhost:5000/is_up``

If you see a page containing the words, "I'm up", you have verified that you
can run the sample app locally.

5. Deploy the sample app to a server accessible from your LTI consumer, edX or
   another LMS.  (These instructions presume you're using edX, but they are
   similar for any LTI consumer.)
#. In edX Studio, navigate to ``Settings\Advanced Settings`` and enter these
   values for the specified keys.

======================= ========================
Keys                    Values
======================= ========================
Advanced Module List    ``[ lti ]``
----------------------- ------------------------
LTI Passports           ``[ "lti_starx_add_demo:__consumer_key__:__lti_secret__" ]``
======================= ========================

7. Still in edX Studio, navigate to the content page that will contain your LTI
   tool and create an LTI Advanced Component.
#. Enter the LTI ID for the external LTI provider.
#. Enter the URL of the external tool that this component launches.

======================= ========================
Keys                    Values
======================= ========================
LTI ID                  ``lti_starx_add_demo``
----------------------- ------------------------
LTI URL                 ``THE_URL_OF_YOUR_DEPLOYED_LTI_PROVIDER``
======================= ========================

.. [#f1] From their website, *"Flask is a microframework for Python based on
   Werkzeug, Jinja 2 and good intentions."* `http://flask.pocoo.org/ <http://flask.pocoo.org/>`_

There is more comprehensive documentation of these settings at
`http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/lti_component.html
<http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/lti_component.html>`_

