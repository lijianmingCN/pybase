# -*- coding: utf-8 -*-
import sys
sys.argv           #命令行参数List，第一个元素是程序本身路径
sys.modules.keys() #返回所有已经导入的模块列表
sys.exc_info()     #获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
sys.exit(0)        #退出程序，正常退出时exit(0)
sys.hexversion     #获取Python解释程序的版本值，16进制格式如：0x020403F0
sys.version        #获取Python解释程序的版本信息
sys.maxint         #最大的Int值
sys.maxunicode     #最大的Unicode值
sys.modules        #返回系统导入的模块字段，key是模块名，value是模块
sys.path           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       #返回操作系统平台名称
sys.stdout         #标准输出
sys.stdin          #标准输入
sys.stderr         #错误输出
sys.exc_clear()    #用来清除当前线程所出现的当前的或最近的错误信息
sys.exec_prefix    #返回平台独立的python文件安装的位置
sys.byteorder      #本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
sys.copyright      #记录python版权相关的东西
sys.api_version    #解释器的C的API版本
sys.version_info   #(2, 4, 3, 'final', 0) 'final'表示最终,也有'candidate'表示候选，表示版本级别，是否有后继的发行
sys.displayhook(value)      #如果value非空，这个函数会把他输出到sys.stdout，并且将他保存进__builtin__._.指在python的交互式解释器里，'_'代表上次你输入得到的结果，hook是钩子的意思，将上次的结果钩过来
sys.getdefaultencoding()    #返回当前你所用的默认的字符编码格式
sys.getfilesystemencoding() #返回将Unicode文件名转换成系统文件名的编码的名字
sys.setdefaultencoding(name)#用来设置当前默认的字符编码，如果name和任何一个可用的编码都不匹配，抛出LookupError，这个函数只会被site模块的sitecustomize使用，一旦别site模块使用了，他会从sys模块移除
sys.builtin_module_names    #Python解释器导入的模块列表
sys.executable              #Python解释程序路径
sys.getwindowsversion()     #获取Windows的版本
sys.stdin.readline()        #从标准输入读一行，sys.stdout.write("a") 屏幕输出a ¬
'''
sys.stdin,sys.stdout,sys.stderr
stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们
从网上摘抄的文章，供大家参考：
#testing stdout

print 'Hello World!'
运行hello.py就会在标准输出的屏幕上打印 Hello World!, 我们再编一个简单的标准输入的小程序 sayhi.py:
#testing stdin

print 'Hi, %s!' % raw_input('Please enter your name:')
当你用键盘输入你的名字后，程序在屏幕上输出Hi，[你的名字]!, 这就是从标准输入：键盘获取信息，再输出到标准输出：屏幕的例子。
那么上面的例子中print 和 raw_input是如何与标准输入/输出流建立关系的呢？
其实Python程序的标准输入/输出/出错流定义在sys模块中，分别 为： sys.stdin, sys.stdout, sys.stderr
上面的程序分别与下列的程序是一样的：
import sys

sys.stdout.write('Hello World!')
import sys

print 'Please enter your name:',
name=sys.stdin.readline()[:-1]
print 'Hi, %s!' % name

那么sys.stdin, sys.stdout, stderr到底是什么呢？我们在Python运行环境中输入以下代码：
import sys
for f in (sys.stdin, sys.stdout, sys.stderr): print f
输出为：
<open file '<stdin>', mode 'r' at 892210>
<open file '<stdout>', mode 'w' at 892270>
<open file '<stderr>', mode 'w at 8922d0>

由此可以看出stdin, stdout, stderr在Python中无非都是文件属性的对象，他们在Python启动时自动与Shell 环境中的标准输入，输出，出错关联。
而Python程序的在Shell中的I/O重定向与本文开始时举的DOS命令的重定向完全相同，其实这种重定向是由Shell来提供的，与Python 本身并无关系。那么我们是否可以在Python程序内部将stdin,stdout,stderr读写操作重定向到一个内部对象呢？答案是肯定的。
Python提供了一个StringIO模块来完成这个设想，比如：
from StringIO import StringIO
import sys
buff =StringIO()

temp = sys.stdout                               #保存标准I/O流
sys.stdout = buff                                 #将标准I/O流重定向到buff对象
print 42, 'hello', 0.001

sys.stdout =temp                                 #恢复标准I/O流
print buff.getvalue()
'''


