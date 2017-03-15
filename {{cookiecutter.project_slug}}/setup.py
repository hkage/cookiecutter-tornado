#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec(open('{{ cookiecutter.project_slug }}/version.py').read())

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

classifiers = """
'Development Status :: 2 - Alpha',
'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
'{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
'Natural Language :: English',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 3.2',
'Programming Language :: Python :: 3.3',
'Programming Language :: Python :: 3.4',
'Programming Language :: Python :: 3.5',
"""


tests_require = [
    'coverage',
    'flake8',
    'pydocstyle',
    'pylint',
    {% if cookiecutter.use_pytest == 'y' -%}
    'pytest-pep8',
    'pytest-cov',
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
    'pytest'{%- endif %}
]

version = '{{ cookiecutter.version }}'

setup(name='{{ cookiecutter.project_name }}',
      version=__version__,
      description='{{ cookiecutter.description }}',
      long_description=read('README.rst'),
      author='{{ cookiecutter.author_name }}',
      author_email='{{ cookiecutter.email }}',
      url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
      classifiers=[c.strip() for c in classifiers.splitlines()
                   if c.strip() and not c.startswith('#')],
      include_package_data=True,
      classifiers=[],
      packages=[
          '{{ cookiecutter.project_slug }}',
          ],
      test_suite='tests',
      setup_requires=['pytest-runner'],
      tests_require=tests_require)
