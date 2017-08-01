# -*- coding: utf-8 -*-
#列表解析
#写法简洁，速度更快、无需计数器来跟踪必须处理的元素
import time
start = time.time()
l = []
for i in range(1000000):
    if i%2 == 0:
        l.append(i)
end = time.time()
print end - start
print '-'*20
start = time.time()
ll = [i for i in range(1000000) if i%2 == 0]
end = time.time()
print end - start
#0.214999914169
#--------------------
#0.15499997139
 
#enumerate
#循环序列时，同时得到索引
l = ['A','B','C','D','E']
for index,element in enumerate(l):
    print index,element
 
#迭代器
#迭代器只不过是一个实现迭代器协议的容器对象。它基于两个方法：
#next 返回容器的下一个项目；
#__iter__ 返回迭代器本身。
first = 'xyz'
second = [1,2,3]
third = ('a','b','c')
ifirst = iter(first)
print ifirst.next()
print ifirst.next()
print ifirst.next()
isecond = iter(second)
print isecond .next(),isecond .next(),isecond .next()
ithird = iter(third)
print ithird.next(),ithird.next(),ithird.next(),ithird.next()

#生成器
def fibnoacci():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b
fib = fibnoacci()
print fib.next()
print fib.next()
#另一只种写法
iter = (i*2 for i in range(10) if i%2 == 0)
for i in iter:
    print i

#装饰器
#对函数或方法的封装（返回一个增强版本的函数）
def pre(fun):
    print 'pre do something'
    return fun
@pre
def main():
    print 'do something'
main()

#range与xrange的区别
for i in range(1000): pass
#会导致生成一个 1000 个元素的 List，而代码：
for i in xrange(1000): pass
#则不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，内存空间占用很小。因为 xrange 不返回 List，而是返回一个 iterable 对象。
 
 