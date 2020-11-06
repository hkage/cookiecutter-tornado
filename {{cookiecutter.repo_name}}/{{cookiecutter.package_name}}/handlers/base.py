# -*- coding: utf-8 -*-

import tornado.web


class MainHandler(tornado.web.RequestHandler):

    # @tornado.web.authenticated
    def get(self):
        self.render('index.html')
