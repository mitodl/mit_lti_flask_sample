Command Line Tools
==================

There are a variety of command line tools you will require to complete this
tutorial.  Most are available by default on Unix-based operating systems like
Linux or OSX.  Some you must explicitly install.

OSX
---

OSX doesn't come with some of these command line tools by default.  Fortunately
they are easy to install on OSX 10.9 Mavericks and newer.  Open the Terminal
application, found in ``/Applications/Utilities/`` and enter:

.. code-block:: bash

  make

These newer versions of OSX recognize that ``make`` is one of the command line
tools not included in the base OSX installation and offers to install all the
command line tools.  This download is free.

In older versions of OSX, you can still open the Terminal application and
enter:

.. code-block:: bash

  xcode-select --install

This command will do the same thing explicitly.

You can also go directly to the Apple Developer site and download the command
line tools directly.  The site will require you to register, but that is free.
This is the URL of the Apple Developer Downloads site:
`https://developer.apple.com/downloads/index.action
<https://developer.apple.com/downloads/index.action>`_ Search for the latest
version of the command line tools for your OSX version.

Linux
-----

Linux systems have a package manager to install new applications and manage
existing ones.  You can check your system's documentation for guidance on its
use.

For debian based systems including Ubuntu you need to run:

.. code-block:: bash

  sudo apt-get install build-essential

For RedHat based distributions, including Fedora and CentOS, run:

.. code-block:: bash

  sudo yum groupinstall "Development Tools"

