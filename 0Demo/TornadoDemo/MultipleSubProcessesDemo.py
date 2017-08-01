# -*- coding: utf-8 -*-
import socket
import tornado.process
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.netutil import bind_sockets

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello')

if __name__ == '__main__':

    sockets = bind_sockets(10000)
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    tornado.process.fork_processes(0) # 0 表示按 CPU 数目创建相应数目的子进程
    server = HTTPServer(app, xheaders=True)
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()