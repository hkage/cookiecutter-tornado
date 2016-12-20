"""Tests for the cookiecutter template."""

from contextlib import contextmanager

from cookiecutter.utils import rmtree


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_project_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project.isdir()
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'Dockerfile' in found_toplevel_files


def test_cookie_secret_has_been_generated(cookies):
    with bake_in_temp_dir(cookies) as result:
        settings_file = result.project.join('settings.py')
        settings_lines = settings_file.readlines(cr=False)
        assert '!!CHANGEME!!' not in settings_lines
        print settings_lines
