import os.path
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec(open('version.py').read())

setup(name='tornado-project-skeleton',
    version=__version__,
    description='Tornado project skeleton',
    long_description=read('README.md'),
    author='Henning Kage',
    author_email='henning.kage@gmail.com',
    url='https://github.com/hkage/tornado-project-skeleton',
    include_package_data=True,
    classifiers=[],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'tornado==4.3'
    ],
    setup_requires=[
        'pytest-runner==2.6.2',
    ],
    tests_require=[
        'pytest==2.8.2',
        'pytest-pep8==1.0.6',
        'pytest-cov==2.2.0',
    ])
