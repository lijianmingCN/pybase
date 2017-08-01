import logging
import tornado
import time
import sys
import signal
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.netutil import bind_sockets

def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)

def shutdown():
    logging.info('Stopping http server')
    server.stop() # 不接收新的 HTTP 请求

    logging.info('Will shutdown in %s seconds ...', settings.MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)
    io_loop = tornado.ioloop.IOLoop.instance()

    deadline = time.time() + settings.MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop() # 处理完现有的 callback 和 timeout 后，可以跳出 io_loop.start() 里的循环
            logging.info('Shutdown')
    stop_loop()

if __name__ == '__main__':
    port = int(sys.argv[1])
    if settings.IPV4_ONLY:
        import socket
        sockets = bind_sockets(port, family=socket.AF_INET)
    else:
        sockets = bind_sockets(port)
    server = HTTPServer(application, xheaders=True)
    server.add_sockets(sockets)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    tornado.ioloop.IOLoop.instance().start()
    logging.info('Exit')
