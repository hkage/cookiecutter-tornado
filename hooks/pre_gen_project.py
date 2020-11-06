# -*- coding: utf-8 -*-

"""Pre generation script"""

import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pre_gen_project')


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
SUPPORTED_PYTHON_VERSIONS = ('2.7', '3.5', '3.6', '3.7', '3.8')

python_versions = [version.strip() for version in '{{ cookiecutter.python_versions }}'.split(',')]


for version in python_versions:
    if version not in SUPPORTED_PYTHON_VERSIONS:
        logger.error('Python {version} is not supported (options are: {options})'.format(
            version=version, options=', '.join(SUPPORTED_PYTHON_VERSIONS)))
        sys.exit(1)
