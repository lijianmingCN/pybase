import threading
import time
import signal
import os


class task_info(object):
    def __init__(self):
        self.func = None
        self.parm0 = None
        self.parm1 = None
        self.parm2 = None


class task_list(object):
    def __init__(self):
        self.tl = []
        self.mutex = threading.Lock()
        self.sem = threading.Semaphore(0)

    def append(self, ti):
        self.mutex.acquire()
        self.tl.append(ti)
        self.mutex.release()
        self.sem.release()

    def fetch(self):
        self.sem.acquire()
        self.mutex.acquire()
        ti = self.tl.pop(0)
        self.mutex.release()
        return ti


class thrd(threading.Thread):
    def __init__(self, tl):
        threading.Thread.__init__(self)
        self.tl = tl

    def run(self):
        while True:
            tsk = self.tl.fetch()
            tsk.func(tsk.parm0, tsk.parm1, tsk.parm2)


class thrd_pool(object):
    def __init__(self, thd_count, tl):
        self.thds = []

        for i in range(thd_count):
            self.thds.append(thrd(tl))

    def run(self):
        for thd in self.thds:
            thd.start()


def func(parm0=None, parm1=None, parm2=None):
    print 'count:%s, thrd_name:%s' % (str(parm0), threading.currentThread().getName())


def cleanup(signo, stkframe):
    print ('Oops! Got signal %s', signo)

    os._exit(0)


if __name__ == '__main__':

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGQUIT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    tl = task_list()
    tp = thrd_pool(6, tl)
    tp.run()

    count = 0
    while True:
        ti = task_info()
        ti.parm0 = count
        ti.func = func
        tl.append(ti)
        count += 1

        time.sleep(2)
    pass
