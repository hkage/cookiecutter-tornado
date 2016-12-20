# -*- coding: utf-8 -*-

"""Post generation script"""

import os
import string
import random


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def generate_random_string(length=25,
                           allowed_chars=string.ascii_letters + string.digits):
    """Generate a random string.

    :param length: The length of the desired string
    :type length: int
    :param allowed_chars: The set of allowed characters
    :type allowed_chars: str
    :returns: Random string
    :rtype: str
    """
    return ''.join(random.choice(allowed_chars) for i in range(length))


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def set_cookie_secret(project_directory):
    project_settings_file = os.path.join(project_directory, 'settings.py')
    with open(project_settings_file) as f:
        file_ = f.read()
    file_ = file_.replace('!!CHANGEME!!', generate_random_string())
    with open(project_settings_file, 'w') as f:
        f.write(file_)


if __name__ == '__main__':
    if '{{ cookiecutter.use_docker }}'.lower() in ('n', 'no'):
        remove_file('Dockerfile')

    if '{{ cookiecutter.use_vagrant }}'.lower() in ('n', 'no'):
        remove_file('Vagrantfile')

    # Replace the cookie secret
    set_cookie_secret(PROJECT_DIRECTORY)
