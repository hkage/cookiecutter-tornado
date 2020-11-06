# -*- coding: utf-8 -*-

"""Global settings for the project"""

import os.path

from tornado.options import define


define("port", default=8000, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

__BASE_PACKAGE__ = "{{ cookiecutter.package_name }}"

settings = {}

settings["debug"] = True
settings["cookie_secret"] = "!!CHANGEME!!"
settings["login_url"] = "/login"
settings["static_path"] = os.path.join(os.path.dirname(__file__), __BASE_PACKAGE__, "static")
settings["template_path"] = os.path.join(os.path.dirname(__file__), __BASE_PACKAGE__, "templates")
settings["xsrf_cookies"] = False
