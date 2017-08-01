# -*- coding: utf-8 -*-
import os

print __file__
print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))
print os.mkdir('/tmp/os_dir',0754)#创建目录
print os.rmdir("/tmp/os_dir") #删除目录
print os.listdir('/root')#列出目录内容
print os.chdir('/tmp')#更改文件目录
#print os.chroot('/tmp') #设置监牢目录
print os.getcwd()#显示当前目录       
print os.makedirs('test/test1/test2')#创建多层目录 类似系统makedir -p
print os.removedirs('/tmp/test/test1/test2')#删除多层目录【每层都是空的除了要删除目录外】
print os.remove("/tmp/testfile")#删除文件
print os.stat('/tmp/os_dir')#查看文件状态
print os.rename('/tmp/os_dir','/tmp/os_rename')#文件夹改名
print os.rename('/tmp/testfile','/tmp/TSFILE') #文件改名
print os.chmod('/tmp/os_rename',0777)#文件权限修改
workspace = os.environ['HOME']
#print os.lchmod(path, mode)#修改连接文件权限
#print os.chown('/tmp/TSFILE',1003,1003)#文件属主修改;uid和gid为-1的时候不改变原来的属主
print os.umask(022)
#print os.walk(topdirpath, topdown=True, onerror=None, followlinks=False)
#参数top表示需要遍历的目录树的路径
#参数topdown的默认值是"True",表示首先返回目录树下的文件，然后在遍历目录树的子目录.Topdown的值为"False"时，则表示先遍历目录树的子目录，返回子目录下的文件，最后返回根目录下的文件
#参数onerror的默认值是"None",表示忽略文件遍历时产生的错误.如果不为空，则提供一个自定义函数提示错误信息后继续遍历或抛出异常中止遍历
#该函数返回一个元组，该元组有3个元素，这3个元素分别表示每次遍历的路径名，目录列表和文件列表dirpath, dirnames, filenames
#对于每个目录树中的目录根在顶部（包括顶部本身，但不包括.和..），产生一个3元组组成的元组对象（dirpath，dirnames，filenames)
#第一元素就是顶层目录，也就是walk方法的第一个参数
#第二元素是顶层目录下子目录的列表
#第三个元素为该目录的文件组成的列表
for root,dir,file in os.walk('/root'):
    [os.path.join(root,name) for name in file]
#这个结果是每个文件和每个文件夹都是一个列表
for root,dir,file in os.walk('/root'):
    for filename in file:
        os.path.join(root,filename)
#这个结果显示每一个文件的路径(包括隐藏文件）
path_collection=[]                                      
for root,dir,file in os.walk('/root'):                  
    for filename in file:                               
        fullpath=os.path.join(root,filename)                 
        path_collection.append(fullpath)
#将目录全部文件的路径，保存到一个列表对象    
for root, dirs, files in os.walk('/root'):
    [os.path.join(root,dirname) for dirname in dirs]
#将根目录和子目录连接在一起

#os.getuid()#
#os.getgid()#
#os.getgroups()# 
#os.getlogin()#当前登陆用户
#os.getpid()#获取当前进程
#os.system(command)#执行操作系统命名
#os.popen(command)#这个方法将命令返回值得保存到一个文件对象里，这个对象需要通过read()等方法读取内容。



'''
###启动新的进程###
>>> import os 
>>> program = "python"
>>> arguments = ["hello.py"]
>>> os.execvp(program, (program,) +  tuple(arguments))
hello again, and welcome to the show
使用的是execvp函数,它会从【标准路径搜索执行程序】,把第二个参数(元组)作为单独的参数传递给程序,并使用当前的环境变量来运行程序. 其他七个同类型函数。
在 Unix 环境下, 你可以通过组合使用 exec , fork 以及 wait 函数来从当前程序调用另一个程序,fork 函数复制当前进程, wait  函数会等待一个子进程执行结束.

###os 模块调用其他程序 (Unix)###
>>> def run(program, *args):
...     pid = os.fork()
...     if not pid:
...             os.execvp(program, (program,) +  args)
...     return os.wait()[0]
>>> run("python", "hello.py")
hello again, and welcome to the show
1701
fork函数在子进程中返回0(这个进程首先从fork返回值),在父进程中返回一个非0的进程标识符(子进程的PID). 也就是说,
只有当我们处于父进程的时候 "not pid" 才为真.(即在子进程中pid为0，pid==0为真，在父进程中not pid(not 0),pid>0为真)
通过os模块中的fork方法，一个进程(Process)可以生成一个独立子进程。fork是一个程序拷贝（copying-program）的过程：
当程序调用fork方法，操作系统生成一份该程序及其在内存中的进程的新的拷贝
，并以与原始程序并行的方式开始执行这份拷贝。原始程序称为父进程，新生成的拷贝叫做子进程。
父进程可以生成任意数目的子进程，子进程还可以生成它的子进程。这些子进程在操作系统的控制下相互独立的并行运行。子进程可以继续运行即便父进程已退出。
>>> def run(program, *args):
...     pid = os.fork()
...     if not pid:
...             os.execvp(program, (program,) +  args)
...     return os.wait()   
... 
>>> run("python", "hello.py")             
hello again, and welcome to the show
(1546, 0)
os.wait() 返回一个元组，这个两个数据代表什么？ 第一元组已完成的子进程号pid，第二个元素为0表示子进程的退出状态
os.wait函数用于等待子进程结束(只适用于UNIX兼容系统)。该函数返回包含两个元素的元组，包括已完成的子进程号pid。
以及子进程的退出状态，返回状态为0，表明子进程成功完成。返回状态为正整数表明子进程终止时出错.
如没有子进程，会引发OSError错误。os.wait
要求父进程等待它的任何一个子进程结束执行，然后唤醒父进程。要指示父进程等候一个指定的子进程终止，可在父进程中使用os.waitpid
函数(只适用于unix兼容系统）.
它可等候一个指定进程结束，然后返回一个双元素元组，其中包括子进程的pid和子进程的退出状态。函数调用将pid
作为第一个参数传递。并将一个选项作为第二个选项，如果第一个参数大于0，则waitpid会等待该pid结束，如果第一个参数是-1
，则会等候所有子进程，也就和os.wait一样
参考http://developer.51cto.com/art/201003/185584.htm
fork和wait 函数在 Windows 上是不可用的, 但是你可以使用 spawn 函数, 不过, spawn 
不会沿着路径搜索可执行文件, 你必须自己处理好这些
   
###os 模块调用其他程序 (Windows)###
os.spawnv(os.P_WAIT, file, (file,) + args)
5、使用 spawn 或 fork/exec 调用其他程序
6、处理守护进程(Daemon Processes)
Unix系统中,你可以使用fork函数把当前进程转入后台(一个"守护者/daemon").一般来说,需要派生(fo
rk off)一个当前进程的副本, 然后终止原进程
import os
import time
pid = os.fork()
if pid:
    os._exit(0) # kill original
print "daemon started"
time.sleep(10)
print "daemon terminated"

###使用os模块终止当前进程###
os._exit(0)

os.getenv('USER',default=None)#获取环境变量
os.putenv(key, value)#修改环境
os.name#判断操作系统
if os.name in ("nt", "dos"):
    exefile = ".exe"
else:
    exefile = "
   

'''


