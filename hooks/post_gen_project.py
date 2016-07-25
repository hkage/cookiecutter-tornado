# -*- coding: utf-8 -*-

"""Post generation script"""

import os


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if '{{ cookiecutter.use_docker }}'.lower() == 'n':
    os.remove(os.path.join(PROJECT_DIRECTORY, 'Dockerfile'))

if '{{ cookiecutter.use_vagrant }}'.lower() == 'n':
    os.remove(os.path.join(PROJECT_DIRECTORY, 'Vagrantfile'))
