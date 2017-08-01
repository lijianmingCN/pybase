# -*- coding: utf-8 -*-
'''
atexit模块很简单，只定义了一个register函数用于注册程序退出时的回调函数，我们可以在这个回调函数中做一些资源清理的操作。

注：如果程序是非正常crash，或者通过os._exit()退出，注册的回调函数将不会被调用。

我们也可以通过sys.exitfunc来注册回调，但通过它只能注册一个回调，而且还不支持参数。
所以建议大家使用atexit来注册回调函数。但千万不要在程序中同时使用这两种方式，否则通过atexit注册的回调可能不会被正常调用。
其实通过查阅atexit的源码，你会发现原来它内部是通过sys.exitfunc来实现的，它先把注册的回调函数放到一个列表中，
当程序退出的时候，按先进后出的顺序调用注册的回调。
如果回调函数在执行过程中抛出了异常，atexit会打印异常的文字信息，并继续执行下一下回调，直到所有的回调都执行完毕，它会重新抛出最后接收到的异常。
'''
import atexit

def exit0(*args, **kwarg):
    print 'exit0'
    for arg in args:
        print ' ' * 4, arg

    for item in kwarg.items():
        print ' ' * 4, item

def exit1():
    print 'exit1'
    raise Exception, 'exit1'

def exit2():
    print 'exit2'

atexit.register(exit0, *[1, 2, 3], **{ "a": 1, "b": 2, })
atexit.register(exit1)
atexit.register(exit2)

@atexit.register
def exit3():
    print 'exit3'

if __name__ == '__main__':
    pass