#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.getcwd())

from fabric.api import *  # noqa


CMD_PYLINT = 'pylint'


@task
def vagrant():
    """Vagrant environment"""
    env.environment = 'local'
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]


@task
def clean():
    """Remove temporary files."""
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.pyc') or name.endswith('~'):
                os.remove(os.path.join(root, name))


@task
def devserver(port=8888, logging='error'):
    """Start the server in development mode."""
    run('python3 run.py --port=%s --logging=%s' % (port, logging))
