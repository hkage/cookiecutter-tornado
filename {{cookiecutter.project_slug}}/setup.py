#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


tests_require = [
    'coverage',
    'flake8',
    'pydocstyle',
    'pylint',
    'pytest-pep8',
    'pytest-cov',
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
    'pytest',
]

version = '{{ cookiecutter.version }}'

setup(name='{{cookiecutter.project_name}}',
      version=version,
      description='{{cookiecutter.description}}',
      long_description=read('README.md'),
      author='{{cookiecutter.author_name}}',
      author_email='{{cookiecutter.email}}',
      url='https://github.com/hkage/tornado-project-skeleton',
      include_package_data=True,
      classifiers=[],
      packages=[
          '{{ cookiecutter.project_slug }}',
          ],
      test_suite='tests',
      setup_requires=['pytest-runner],
      tests_require=tests_require)
