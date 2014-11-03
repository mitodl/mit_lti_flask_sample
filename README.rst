Sample LTI Provider for Flask
=============================

This is a sample LTI provider for the Flask framework.  It is one of a series of
LTI providers written for popular frameworks.  Each of these samples consumes
the pylti module.  You will need both this app and the pylti module to run
the sample.

By creating an interface boundary between the provider and
the library, each sample contains only the code variations necessary to support
its specific framework.  Since the interface to the pylti module remains the
same for each, you may easily switch your custom provider from one framework to
another.

Please see the pylti `README <https://github.com/mitodl/pylti>`_ for a
detailed description of the architecture.
