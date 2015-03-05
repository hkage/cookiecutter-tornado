from setuptools import setup, find_packages


setup(name='tornado-project-skeleton',
      version='0.1',
      description='Tornado project skeleton',
      long_description='',
      author='Henning Kage',
      author_email='henning.kage@gmail.com',
      url='https://github.com/hkage/tornado-project-skeleton',
      include_package_data=True,
      classifiers=[],
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'tornado==4.1'
      ],
      tests_require=[
          'pytest>=2.6.0',
          'pytest-pep8',
          'pytest-cov',
          'tox'
      ])
