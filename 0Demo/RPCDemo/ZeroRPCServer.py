import zerorpc
import time
class HelloRPC(object):
    def hello(self, name):
        print   "this is %s  %s" %(name,time.strftime('%Y-%m-%d %H-%m-%S',time.localtime(time.time())))
        return "Hello, %s" %time.strftime('%Y-%m-%d %H-%m-%S',time.localtime(time.time()))
s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()