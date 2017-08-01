# -*- coding: utf-8 -*-
import tornado.web
import tornado.wsgi
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

tornado_app = tornado.web.Application([
    (r"/", MainHandler),
])
application = tornado.wsgi.WSGIAdapter(tornado_app)
#然后将要托管的应用以参数的形式传入到WSGIContainer类中
container = tornado.wsgi.WSGIContainer(application)
#接下来,我们定义1个HTTP服务器,用于提供服务
http_server = tornado.httpserver.HTTPServer(container)
#紧接着,我们定义这个服务器监听的端口
http_server.listen(8888)
#最后,我们启动这个服务器
tornado.ioloop.IOLoop.current().start()