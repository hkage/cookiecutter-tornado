# -*- coding: utf-8 -*-

"""Pre generation script"""

import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pre_gen_project')


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
SUPPORTED_PYTHON_VERSIONS = ('3.6', '3.7', '3.8', '3.9', '3.10')

python_versions = [version.strip() for version in '{{ cookiecutter.python_versions }}'.split(',')]


for version in python_versions:
    if version not in SUPPORTED_PYTHON_VERSIONS:
        logger.error('Python %s is not supported (options are: %s)', version, ', '.join(SUPPORTED_PYTHON_VERSIONS))
        sys.exit(1)
