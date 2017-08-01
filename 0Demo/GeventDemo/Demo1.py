import gevent

import gevent.monkey
gevent.monkey.patch_all()
#gevent.monkey.patch_all()的作用是将一些常见的阻塞，如socket、select等会阻塞的地方实现协程跳转，而不是在那里一直等待，导致整个协程组无法工作。

def foo(i, a, b, c):
    print('Running in foo' + str(i) + ' ' + str(a) + str(b) + str(c))
    gevent.sleep(0)
    print('Explicit context switch to foo again')

tasks = [ gevent.spawn(foo,i, 1, 2,3) for i in range(0,10)]
gevent.joinall(tasks)