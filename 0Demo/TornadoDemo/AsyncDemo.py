# -*- coding: utf-8 -*-
import time
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
from tornado.options import define, options
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
import time

'''
没有使用异步:
先访问http://localhost:9000/sleep,
再访问http://localhost:9000/justnow.
你会发现本来可以立刻返回的/jsutnow的请求会一直阻塞到/sleep请求完才返回.
使用异步后:
打开/sleep之后再点击/justnow， justnow的请求都是立刻返回不受影响
'''
define("port", default=9000, help="run on the given port", type=int)


class A(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        yield self.do()

    def do(self):
        time.sleep(10)
        return self.write('AAA')

class SleepHandler(tornado.web.RequestHandler):
    # 线程池
    executor = ThreadPoolExecutor(10)

    # 线程里处理
    @run_on_executor
    def my_func(self):
        # do something with data
        time.sleep(10)
        return 'hello'

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # 获取各种参数
        res = yield self.my_func()
        self.write(str(res))
        self.finish()

class JustNowHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("i hope just now see you")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/c", A),
        (r"/a", SleepHandler),
        (r"/b", JustNowHandler),

    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/' % options.port
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()
