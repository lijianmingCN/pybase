# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define, options
from tornado.web import Application
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello Tornado!!!')

settings = {
    "cookie_secret" : "BaiDuTieBaQA",
    "template_path" : os.path.join(os.path.dirname(__file__), "template"),
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True,
    "gzip" : True
}

url = [
    (r"/", IndexHandler),
]
application = Application(url, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()