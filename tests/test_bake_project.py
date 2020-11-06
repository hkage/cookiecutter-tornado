"""Tests for the cookiecutter template."""

from contextlib import contextmanager

import pytest
from cookiecutter.utils import rmtree


YES_NO_CHOICES = [
    ('y', True),
    ('yes', True),
    ('YES', True),
    ('n', False),
    ('no', False),
    ('NO', False),
]


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    extra_context = kwargs.setdefault('extra_context', {})
    extra_context.setdefault('project_name', 'myproject')
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project), ignore_errors=True)


def test_bake_project_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project.isdir()
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'Dockerfile' in found_toplevel_files
        assert 'tests' in found_toplevel_files


@pytest.mark.parametrize('with_docker_support, expected_result', YES_NO_CHOICES)
def test_docker_support(cookies, with_docker_support, expected_result):
    with bake_in_temp_dir(cookies, extra_context={'use_docker': with_docker_support}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ('Dockerfile' in found_toplevel_files) == expected_result


@pytest.mark.parametrize('with_vagrant_support, expected_result', YES_NO_CHOICES)
def test_vagrant_support(cookies, with_vagrant_support, expected_result):
    with bake_in_temp_dir(cookies, extra_context={'use_vagrant': with_vagrant_support}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ('Vagrantfile' in found_toplevel_files) == expected_result


@pytest.mark.parametrize('with_bumpversion_support, expected_result', YES_NO_CHOICES)
def test_bumpversion_support(cookies, with_bumpversion_support, expected_result):
    with bake_in_temp_dir(cookies, extra_context={'use_bumpversion': with_bumpversion_support}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ('.bumpversion.cfg' in found_toplevel_files) == expected_result


@pytest.mark.parametrize('with_pytest_support, expected_result', YES_NO_CHOICES)
def test_pytest_support(cookies, with_pytest_support, expected_result):
    with bake_in_temp_dir(cookies, extra_context={'use_pytest': with_pytest_support}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ('pytest.ini' in found_toplevel_files) == expected_result


@pytest.mark.parametrize('with_tox_support, expected_result', YES_NO_CHOICES)
def test_tox_support(cookies, with_tox_support, expected_result):
    with bake_in_temp_dir(cookies, extra_context={'use_tox': with_tox_support}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ('tox.ini' in found_toplevel_files) == expected_result


def test_cookie_secret_has_been_generated(cookies):
    with bake_in_temp_dir(cookies) as result:
        settings_file = result.project.join('settings.py')
        settings_lines = settings_file.readlines(cr=False)
        assert '!!CHANGEME!!' not in settings_lines


def test_without_internationalization(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'use_i18n': 'No'}
    ) as result:
        assert result.project.join('myproject/locale').isdir() is False
