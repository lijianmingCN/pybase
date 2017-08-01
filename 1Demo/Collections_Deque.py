# -*- coding: utf-8 -*-
from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print elem.upper()
d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print d
print d.pop()                          # return and remove the rightmost item
print d.popleft()                      # return and remove the leftmost item
print d.count('j')
print list(d)                          # list the contents of the deque
print d[0]                             # peek at leftmost item
print d[-1]                            # peek at rightmost item
print list(reversed(d))                # list the contents of a deque in reverse
print 'h' in d                         # search the deque
print d.extend('jkl')                  # add multiple elements at once
print d.extendleft('000')
print d.rotate(1)                      # right rotation
print d.rotate(-1)                     # left rotation
print deque(reversed(d))               # make a new deque in reverse order
d.clear()                        # empty the deque
d.extendleft('abc')              # extendleft() reverses the input order
print d






#双端队列deque
d = deque('abcdefg')
d.extend('RRR')#右侧合并
d.append('RRR')#右侧追加
d.extendleft('LLL')#左侧合并
d.appendleft('LLL')#左侧追加
d.pop()#右侧删除，返回删除的值
d.popleft()()#左侧删除，返回删除的值
#deque线程安全的，甚是可以不同线程中同时从两端利用队列内容
import collections
import threading
import time
candle = collections.deque(xrange(10))
def burn(direction,nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print '%8s:%s'%(direction,next)
        time.sleep(0.1)
    print '%8s done'% direction
    return
left = threading.Thread(target=burn,args=('Left',candle.popleft))
right = threading.Thread(target=burn,args=('Right',candle.pop))
left.start()
right.start()
left.join()
right.join()
#旋转
d.rotate(2)#右旋2位
d.rotate(-2)#左旋2位