MIT's Sample LTI Provider for Flask
===================================

This is a sample LTI provider for the Flask framework.  It is a minimal
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

Contents
--------

.. toctree::
   :maxdepth: 2

   tutorial
   deploy_to_heroku
   cmd_line_tools
   license


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

