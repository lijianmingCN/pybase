# -*- coding: utf-8 -*-
import threading
import random
import time
#后台线程
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        wait_time=random.randrange(1,10)
        time.sleep(wait_time)
        print "子进程 %s 结束!" % self.name

if __name__=="__main__":
    print '主进程开始!'
    threads = []
    for i in range(5):
        t = MyThread()
        t.setDaemon(False)
        t.start()
        threads.append(t)
    #for t in threads:
    #    t.join()
    print '主进程结束!'

