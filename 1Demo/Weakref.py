# -*- coding: utf-8 -*-
#非永久引用
import weakref,gc
#引用
class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)'%self

obj = ExpensiveObject()
r = weakref.ref(obj)
print 'obj:',obj
print 'ref',r
print 'r():',r()
print 'deleting obj'
del obj
print 'r():',r()
'''
#引用回调
class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)'%self
def callback(reference):
    print 'callback:',reference
obj = ExpensiveObject()
r = weakref.ref(obj,callback)
print 'obj:',obj
print 'ref',r
print 'r():',r()
print 'deleting obj'
del obj
print 'r():',r()

#代理
class ExpensiveObject(object):
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print '(Deleting %s)'%self
obj = ExpensiveObject('My Object')
r = weakref.ref(obj)
p = weakref.proxy(obj)
print obj.name
print r().name
print p.name
del obj
print p.name
#循环引用
#缓存对象
'''

