# -*- coding: utf-8 -*-

"""Post generation script"""

import os
import random
import shutil
import string


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_FILES = ('Dockerfile', '.dockerignore', 'docker-compose.yml')
VAGRANT_FILES = ('Vagrantfile', 'bootstrap.sh')


def generate_random_string(length=25,
                           allowed_chars=string.ascii_letters + string.digits):
    """
    Generate a random string.

    :param length: The length of the desired string
    :type length: int
    :param allowed_chars: The set of allowed characters
    :type allowed_chars: str
    :returns: Random string
    :rtype: str
    """
    return ''.join(random.choice(allowed_chars) for i in range(length))


def remove_file(filepath):
    """
    Remove a file with the given path.

    :param str filepath: Path of the file.
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def set_cookie_secret(project_directory):
    """
    Open the settings and generate a secure cookie secret.

    :param str project_directory: Path of the project directory.
    """
    project_settings_file = os.path.join(project_directory, 'settings.py')
    with open(project_settings_file) as f:
        file_ = f.read()
    file_ = file_.replace('!!CHANGEME!!', generate_random_string())
    with open(project_settings_file, 'w') as f:
        f.write(file_)


if __name__ == '__main__':
    if '{{ cookiecutter.use_docker }}' != 'Yes':
        for filename in DOCKER_FILES:
            remove_file(filename)

    if '{{ cookiecutter.use_vagrant }}' != 'Yes':
        for filename in VAGRANT_FILES:
            remove_file(filename)

    if '{{ cookiecutter.use_tox }}' != 'Yes':
        remove_file('tox.ini')

    if '{{ cookiecutter.use_pytest }}' != 'Yes':
        remove_file('pytest.ini')

    if '{{ cookiecutter.use_i18n }}' != 'Yes':
        shutil.rmtree('{{ cookiecutter.package_name }}/locale', ignore_errors=True)

    # Replace the cookie secret
    set_cookie_secret(PROJECT_DIRECTORY)
