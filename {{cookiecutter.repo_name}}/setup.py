{%- set python_versions = cookiecutter.python_versions.split(",") -%}
#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import distutils
import subprocess
from os.path import dirname, join

from setuptools import setup, find_packages
{%- if cookiecutter.use_i18n == "Yes" %}
from setuptools.command.sdist import sdist
from wheel.bdist_wheel import bdist_wheel
{%- endif %}


def read(*args):
    return open(join(dirname(__file__), *args)).read()

{%- if cookiecutter.use_tox == "Yes" %}

class ToxTestCommand(distutils.cmd.Command):
    """Distutils command to run tests via tox with 'python setup.py test'.

    Please note that in our standard configuration tox uses the dependencies in
    `requirements/dev.txt`, the list of dependencies in `tests_require` in
    `setup.py` is ignored!

    See https://docs.python.org/3/distutils/apiref.html#creating-a-new-distutils-command
    for more documentation on custom distutils commands.
    """
    description = "Run tests via 'tox'."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.announce("Running tests with 'tox'...", level=distutils.log.INFO)
        return subprocess.call(['tox'])
{%- endif %}

{%- if cookiecutter.use_i18n == "Yes" %}


def compile_translations(self):
    """
    Wrapper around the `run` method of distutils or setuptools commands.

    The method creates the compiled translation files before the `run` method of the superclass is run.
    """
    self.announce("Compiling translations", level=distutils.log.INFO)
    self.run_command('compile_catalog')
    super(self.__class__, self).run()


def command_factory(name, base_class, wrapper_method):
    """Factory method to create a distutils or setuptools command with a patched `run` method."""
    return type(str(name), (base_class, object), {'run': wrapper_method})
{%- endif %}


exec(open('{{ cookiecutter.package_name }}/version.py').read())

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

install_requires = [
]

tests_require = [
    'coverage',
    'flake8',
    'pydocstyle',
    'pylint',
    {% if cookiecutter.use_pytest == "Yes" -%}
    'pytest-pep8',
    'pytest-cov',
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
    'pytest'{%- endif %}
]

exec(read('{{ cookiecutter.package_name }}', 'version.py'))


setup(name='{{ cookiecutter.project_name }}',
      version=__version__,  # noqa
      description='{{ cookiecutter.description }}',
      long_description=read('README.rst'),
      author='{{ cookiecutter.author_name }}',
      author_email='{{ cookiecutter.email }}',
      url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
      classifiers=[
          'Development Status :: 2 - Alpha',
          'Intended Audience :: Developers',
          {%- if cookiecutter.open_source_license in license_classifiers %}
          '{{ license_classifiers[cookiecutter.open_source_license] }}',
          {%- endif %}
          'Natural Language :: English',
          'Programming Language :: Python',
          {% for version in python_versions -%}
          'Programming Language :: Python :: {{ version|trim }}',
          {% endfor -%}
          'Topic :: Internet'
      ],
      include_package_data=True,
      install_requires=install_requires,
      packages=find_packages(include=['{{ cookiecutter.package_name }}*']),
      test_suite='tests',
      setup_requires=['pytest-runner'],
      tests_require=tests_require,
      cmdclass={
        {%- if cookiecutter.use_tox == "Yes" %}
        'test': ToxTestCommand,
        { % - endif %}
        {%- if cookiecutter.use_i18n == "Yes" %}
        'sdist': command_factory('SDistCommand', sdist, compile_translations),
        'bdist_wheel': command_factory('BDistWheelCommand', bdist_wheel, compile_translations),
        {%- endif %}
    }
)
