# -*- coding: utf-8 -*-
#函数式编程Map
def fun(x):
    return x*x
print map(fun, [1,2,3,4,5,6,7,8,9])

#函数式编程Reduce
def add(x, y):
    return x+y
print reduce(add, [1,3,5,7,9])

#函数式编程lambda
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#函数式编程filter
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

#装饰器
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper




