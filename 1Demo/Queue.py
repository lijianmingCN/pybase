# -*- coding: utf-8 -*-

'''可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。
将一个值放入队列中
myqueue.put(10)
调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为1。
如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。
将一个值从队列中取出
myqueue.get()
调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
如果队列为空且block为False，队列将引发Empty异常。
Queue.qsize() 返回队列的大小 
Queue.empty() 如果队列为空，返回True,反之False 
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应 
Queue.get([block[, timeout]])获取队列，timeout等待时间 
Queue.get_nowait() 相当Queue.get(False)
非阻塞 Queue.put(item) 写入队列，timeout等待时间 
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作 
'''
import Queue
#FIFO
q = Queue.Queue(maxsize = 100)
for i in range(5):
    q.put(i)
while not q.empty():
    print q.get()
#LIFO
q = Queue.LifoQueue()
for i in range(5):
    q.put(i)
while not q.empty():
    print q.get()
    
    
#优先队列
import Queue
import threading
class Job(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
        print 'New Job:',description
        return
    def __cmp__(self,other):
        return cmp(self.priority,other.priority)
q = Queue.PriorityQueue()
q.put(Job(3,'Mid-level job'))
q.put(Job(10,'Low-level job'))
q.put(Job(1,'Important job'))
def process_job(q):
    while True:
        next_job = q.get()
        print 'Processing job:',next_job.description
        q.task_done()
workers = [threading.Thread(target=process_job,args=(q,)),
           threading.Thread(target=process_job,args=(q,))]
for w in workers:
    w.setDaemon(True)
    w.start()

'''
1. 阻塞模式

import Queue

q = Queue.Queue(10)

......
       for i in range(10):
               q.put('A')
               time.sleep(0.5)
这是一段极其简单的代码（另有两个线程也在操作队列q），我期望每隔0.5秒写一个'A'到队列中，
但总是不能如愿：间隔时间有时会远远超过0.5秒。原来，Queue.put（）默认有 block = True 和 timeou 两个参数。
当  block = True 时，写入是阻塞式的，阻塞时间由 timeou  确定。
当队列q被（其他线程）写满后，这段代码就会阻塞，直至其他线程取走数据。Queue.put（）方法加上 block=False 的参数，
即可解决这个隐蔽的问题。但要注意，非阻塞方式写队列，当队列满时会抛出 exception Queue.Full 的异常。

2. 无法捕获 exception Queue.Empty 的异常

while True:
                ......
                try:
                        data = q.get()
                except Queue.Empty:
                        break

我的本意是用队列为空时，退出循环，但实际运行起来，却陷入了死循环。
这个问题和上面有点类似：Queue.get（）默认的也是阻塞方式读取数据，队列为空时，不会抛出 except Queue.Empty ，而是进入阻塞直至超时。
 加上block=False 的参数，问题迎刃而解。
'''

'''
另外请问一下使用

queue.join()
queue.task_done()
和

while not workQueue.empty():
    pass
这两种方式来判断队列中是否还有任务的机制有区别吗？哪种更好呢？


具体要看你的设计和使用场景。
queue.join会一直阻塞，直到队列中所有的message都被get出来并且调用task_done才会返回。通常用在等待所有的任务都处理完了，然后退出进程。
empty会立马返回，用你的while循环检查时，如果队列为空线程会一直用死循环。循环等待会很耗CPU。


'''