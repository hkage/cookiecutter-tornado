# -*- coding: utf-8 -*-

from .handlers import base


url_patterns = [
    (r'/', base.MainHandler),
]