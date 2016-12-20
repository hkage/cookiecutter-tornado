Tornado Cookiecutter template
===

[![Build Status](https://travis-ci.org/hkage/cookiecutter-tornado.svg?branch=development)](https://travis-ci.org/hkage/cookiecutter-tornado)

This is my cookiecutter template to build a simple, fast and rock solid website based upon
the Tornado framework. There are quite many Tornado template projects out there,
but I wanted to start something from scratch, that fits my needs and evolves out
of years of experiences (positive and negative alike) with other Python based webframeworks like Turbogears and Django.

Of course this template is not designed for larger data structures. The main
focus is on scalability, fast data access and small library dependencies.

Features
---
* Configurable as a Cookiecutter template
* pytest and tox for testing
* Basic [HTML5 Boilerplate](https://html5boilerplate.com/)
* SASS for CSS generation
* (Optional) [Bumpversion](https://github.com/peritus/bumpversion) for updating version information
* (Optional) Vagrant and Docker support

Installation
---

Install Cookiecutter

    $ pip install cookiecutter

Initialize the project with cookiecutter and answer some questions for the newly started project:

    $ cookiecutter https://github.com/hkage/cookiecutter-tornado

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
start the development server with the following command:

    $ vagrant up
    $ fab vagrant devserver

You can now access your application via `http://localhost:8000`

Docker
---

To run the application within Docker, you need to build and then run the image:

    $ sudo docker build --tag=tornado-app --rm=true .
    $ sudo docker run -p 8000:8000 -t -i tornado-app:latest

You can now access your application via `http://localhost:8000`
