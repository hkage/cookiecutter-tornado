Tornado project skeleton
===

This is my boilerplate to build a simple, fast and rock solid website based upon
the Tornado framework. There are quite many Tornado template projects out there,
but I wanted to start something from scratch, that fits my needs and evolves out
of years of experiences (positive and negative alike) with other Python based webframeworks like Turbogears and Django.

Of course this template is not designed for larger data structures. The main
focus is on scalability, fast data access and small library dependencies.

Features
---
* pytest for testing
* Vagrant file supported

Installation
---

Check out the sources and install the requirements:

    $ git clone git@github.com:hkage/tornado-project-skeleton.git
    $ python setup.py install

Configuration
---

Testing
---
All test files will be added to the ``tests`` directory. To run the tests, simply call:

    $ python setup.py test

Start the server
---

To start the final application, just run the following fabric command:

    $ fab devserver

This will tell Tornado to start the applicaton with the default port 8888. If
you want to use another port, just type:

    $ fab devserver:port=8000

In addition to that, see the fabfile.py Script for other parameters and
commands.

Using vagrant
---

To run the server within a Vagrant VM, you need to install Vagrant 1.7.x and
start the development server with the following command::

    $ fab vagrant devserver
