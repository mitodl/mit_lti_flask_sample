Tutorial: Setup edX
===================

The intent of this tutorial is to show how to:

    * Create a virtual environment to run an edX server locally
    * Download edX and run an
    * Run a sample course in edX

References:

    https://github.com/edx/configuration/wiki/edX-Production-Stack

Create a virtual environment and run an edX server in it
********************************************************

Download and install Vagrant and VirtualBox from:

    http://www.vagrantup.com/downloads
    https://www.virtualbox.org/wiki/Downloads

If you previously installed Vagrant and VirtualBox and you have
no reason to preserve existing Vagrant/VirtualBox instances:

    Run VirtualBox and remove all vagrant instances.
    Remove unused VMs from VirtualBox VMs.
    Reboot your machine to insure that you are off to a clean start.

To ``INSTALL`` the edX production stack in a Terminal Window
(the edX production installation is lengthy and takes a while)::

    $ mkdir fullstack
    $ cd fullstack
    $ curl -L https://raw.githubusercontent.com/edx/configuration/master/vagrant/release/fullstack/Vagrantfile > Vagrantfile
    $ vagrant plugin install vagrant-hostsupdater
    $ vagrant up

    The ``vagrant up`` will complete the installation and start edX VM.
    At this point you can leave the Terminal Window and the edX VM will
    continue to be active.

To ``ACTIVATE`` the edX server on an existing VM::

    $ vagrant up

To ``DEACTIVATE`` a running edX server::

    $ vagrant halt


Default username/password: vagrant/vagrant

Run a sample course in edX
**************************

Once the VM is running, you can access the LMS and Studio at these URLS:

        LMS: http://192.168.33.10/
        Studio: http://192.168.33.10:18010/
        The basic auth user and password are both set to "edx"

