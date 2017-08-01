# -*- coding: utf-8 -*-
import ssl,os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.options import define, options

define("port", default=7000, help="run on the given port", type=int)

class TestHandler(RequestHandler):
    def get(self):
        self.write('Hello Https!!!')


settings = {
    "cookie_secret" : "BaiDuTieBaQA",
    "template_path" : os.path.join(os.path.dirname(__file__), "template"),
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True,
    "gzip" : True
}
url = [
    (r"/", TestHandler),
]
application = Application(url, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()

    server = HTTPServer(application,ssl_options={
           "certfile": os.path.join(os.path.abspath("."), "ssl-key/mycert1.cer"),
           "keyfile": os.path.join(os.path.abspath("."), "ssl-key/mycert1.key"),
       })

    server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()

