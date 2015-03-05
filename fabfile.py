#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import os
import sys
sys.path.insert(0, os.getcwd())

from fabric import colors
from fabric.api import *  # NOQA
from fabric.contrib.console import confirm

# be compatible with fabric 1.0
try:
    task
except NameError:
    task = lambda f: f


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
    run('python run.py --port=%s --logging=%s' % (port, logging))


@task
def mo():
    pass


@task
def po():
    pass


@task
def pylint(pylint_cmd=CMD_PYLINT, pylint_options=None):
    if pylint_options is None:
        pylint_options = []
    with settings(warn_only=True):
        result = local(' '.join([CMD_PYLINT, '--rcfile=tools/pylint.rc']
                                +pylint_options))
        fatal = 1
        error = 2
        warning = 4
        usage = 32
        if result.return_code == usage:
            abort(colors.red('Pylint usage error.', bold=True))
        elif fatal & result.return_code or error & result.return_code:
            abort(colors.red('Pylint error.', bold=True))
        elif warning & result.return_code:
            print(colors.yellow('Pylint reported warnings.'))


@task
def test():
    pass
