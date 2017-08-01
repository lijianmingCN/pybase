# coding:utf-8
from rpyc import Service
from rpyc.utils.server import ThreadedServer

class TestService(Service):
    # 对于服务端来说， 只有以"exposed_"打头的方法才能被客户端调用，所以要提供给客户端的方法都得加"exposed_"
    def exposed_test(self, num):
        return 1+num

sr = ThreadedServer(TestService, port=9911, auto_register=False)
sr.start()

'''
异步调用基本使用过程：
async_function_obj=rpyc.async(c.root.get_time) #关联一个异步对象到目标函数
result_obj=async_function() #通知服务端在适当的时候调用目标函数
if result_obj.ready: #查询服务端是否已经完成了函数调用
print result_obj.value #打印函数返回值

回调函数：让服务端在完成目标函数调用后，调用一个客户端函数。此时客户端将自己的一个函数对象传递给服务端函数作为一个参数，服务端函数完成工作后调用此函数。
事件通知：客户端如果不处理任何返回值，可以作为事件通知机制，通知服务端运行某函数。

（异步的工作交与服务端处理了。）

rpyc/servers/classic_server.py
rpyc/servers/registry_server.py
内置的两个工具这个就有点像Django的工具一样的！

registry-server类似于dns服务器，简化了对rpyc服务所在ip、端口的记忆。
在一个局域网中只需要一个此服务，一旦局域网中有一个主机运行了registry-server.py，那么我们就可以使用名字来连接服务。
将IP与端口与域名进行了绑定处理。

RPYC—自带服务—classic_server.py
提供的功能：
eval
execute
modules
使用：c.root.eval或c.eval（对classic_server特例）来访问
客户端访问：
c=rpyc.classic.connect(“localhost”) #连接
c.modules.os.system(‘ls’) #用modules可访问任何服务端库
c.eval(‘1+23’) #简单python语句执行

认证:
(在编写RMI程序的时候就需要有一个认证的过程)
1：
服务端提供：
def exposed_login(user,pass) 函数
def exposed_logout()函数
其他exposed函数中检查用户是否登录，没有登录则直接返回。

RPYC提供了两个服务：
ThreadedServer
ForkingServer

服务可调用函数有：
start
register
unregister
close
fileno


'''