# -*- coding: utf-8 -*
'''
这里的内容以Linux进程基础和Linux文本流为基础。subprocess包主要功能是执行外部的命令和程序。比如说，我需要使用wget下载文件。我在Python中调用wget程序。从这个意义上来说，subprocess的功能与shell类似。
1. subprocess以及常用的封装函数
当我们运行python的时候，我们都是在创建并运行一个进程。正如我们在Linux进程基础中介绍的那样，一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。在Python中，我们通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序(fork，exec见Linux进程基础)。
subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。
使用subprocess包中的函数创建子进程的时候，要注意:
1) 在创建子进程之后，父进程是否暂停，并等待子进程运行。
2) 函数返回什么
3) 当returncode不为0时，父进程如何处理。 
subprocess.call()
父进程等待子进程完成
返回退出信息(returncode，相当于exit code，见Linux进程基础)
subprocess.check_call()
父进程等待子进程完成
返回0
检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try...except...来检查(见Python错误处理)。
subprocess.check_output()
父进程等待子进程完成
返回子进程向标准输出的输出结果
检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try...except...来检查。
这三个函数的使用方法相类似，我们以subprocess.call()来说明:
import subprocess
rc = subprocess.call(["ls","-l"])
我们将程序名(ls)和所带的参数(-l)一起放在一个表中传递给subprocess.call()
可以通过一个shell来解释一整个字符串:
import subprocess
out = subprocess.call("ls -l", shell=True)
out = subprocess.call("cd ..", shell=True)
我们使用了shell=True这个参数。这个时候，我们使用一整个字符串，而不是一个表来运行子进程。Python将先运行一个shell，再用这个shell来解释这整个字符串。
shell命令中有一些是shell的内建命令，这些命令必须通过shell运行，$cd。shell=True允许我们运行这样一些命令。
2. Popen
实际上，我们上面的三个函数都是基于Popen()的封装(wrapper)。这些封装的目的在于让我们容易使用子进程。当我们想要更个性化我们的需求的时候，就要转向Popen类，该类生成的对象用来代表子进程。
与上面的封装不同，Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)：
import subprocess
child = subprocess.Popen(["ping","-c","5","www.baidu.com"])
print("parent process")
从运行结果中看到，父进程在开启子进程之后并没有等待child的完成，而是直接运行print。
对比等待的情况:
import subprocess
child = subprocess.Popen(["ping","-c","5","www.google.com"])
child.wait()
print("parent process") 
此外，你还可以在父进程中对子进程进行其它操作，比如我们上面例子中的child对象:
child.poll()           # 检查子进程状态
child.kill()           # 终止子进程
child.send_signal()    # 向子进程发送信号
child.terminate()      # 终止子进程
子进程的PID存储在child.pid
3. 子进程的文本流控制
(沿用child子进程) 子进程的标准输入，标准输出和标准错误也可以通过如下属性表示:
child.stdin
child.stdout
child.stderr
我们可以在Popen()建立子进程的时候改变标准输入、标准输出和标准错误，并可以利用subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe):
import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)
out = child2.communicate()
print(out)
subprocess.PIPE实际上为文本流提供一个缓存区。child1的stdout将文本输出到缓存区，随后child2的stdin从该PIPE中将文本读取走。child2的输出文本也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本。
要注意的是，communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成。
我们还可以利用communicate()方法来使用PIPE给子进程输入:
import subprocess
child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child.communicate("vamei")我们启动子进程之后，cat会等待输入，直到我们用communicate()输入"vamei"。
通过使用subprocess包，我们可以运行外部程序。这极大的拓展了Python的功能。
如果你已经了解了操作系统的某些应用，你可以从Python中直接调用该应用(而不是完全依赖Python)，并将应用的结果输出给Python，并让Python继续处理。
shell的功能(比如利用文本流连接各个应用)，就可以在Python中实现




subprocess模块中只定义了一个类: Popen。可以使用Popen来创建进程，并与进程进行复杂的交互。它的构造函数如下：
subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
　　参数args可以是字符串或者序列类型（如：list，元组），用于指定进程的可执行文件及其参数。如果是序列类型，第一个元素通常是可执行文件的路径。我们也可以显式的使用executeable参数来指定可执行文件的路径。在windows操作系统上，Popen通过调用CreateProcess()来创建子进程,CreateProcess接收一个字符串参数，如果args是序列类型，系统将会通过list2cmdline()函数将序列类型转换为字符串。
　　参数bufsize：指定缓冲。我到现在还不清楚这个参数的具体含义，望各个大牛指点。
　　参数executable用于指定可执行程序。一般情况下我们通过args参数来设置所要运行的程序。如果将参数shell设为True，executable将指定程序使用的shell。在windows平台下，默认的shell由COMSPEC环境变量来指定。
　　参数stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
　　参数preexec_fn只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用。
　　参数Close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。我们不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
　　如果参数shell设为true，程序将通过shell来执行。
　　参数cwd用于设置子进程的当前目录。
　　参数env是字典类型，用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
　　参数Universal_newlines:不同操作系统下，文本的换行符是不一样的。如：windows下用'\r\n'表示换，而Linux下用'\n'。如果将此参数设置为True，Python统一把这些换行符当作'\n'来处理。
　　参数startupinfo与createionflags只在windows下用效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等。 
subprocess.PIPE
　　在创建Popen对象时，subprocess.PIPE可以初始化stdin, stdout或stderr参数。表示与子进程通信的标准流。
subprocess.STDOUT
　　创建Popen对象时，用于初始化stderr参数，表示将错误通过标准输出流输出。 
Popen的方法：
Popen.poll() 
　　用于检查子进程是否已经结束。设置并返回returncode属性。
Popen.wait() 
　　等待子进程结束。设置并返回returncode属性。
Popen.communicate(input=None)
　　与子进程进行交互。向stdin发送数据，或从stdout和stderr中读取数据。可选参数input指定发送到子进程的参数。Communicate()返回一个元组：(stdoutdata, stderrdata)。
    注意：如果希望通过进程的stdin向其发送数据，在创建Popen对象的时候，参数stdin必须被设置为PIPE。同样，如果希望从stdout和stderr获取数据，必须将stdout和stderr设置为PIPE。
Popen.send_signal(signal) 
　　向子进程发送信号。
Popen.terminate()
　　停止(stop)子进程。在windows平台下，该方法将调用Windows API TerminateProcess（）来结束子进程。
Popen.kill()
　　杀死子进程。
Popen.stdin 
　　如果在创建Popen对象是，参数stdin被设置为PIPE，Popen.stdin将返回一个文件对象用于策子进程发送指令。否则返回None。
Popen.stdout 
　　如果在创建Popen对象是，参数stdout被设置为PIPE，Popen.stdout将返回一个文件对象用于策子进程发送指令。否则返回None。
Popen.stderr 
　　如果在创建Popen对象是，参数stdout被设置为PIPE，Popen.stdout将返回一个文件对象用于策子进程发送指令。否则返回None。
Popen.pid 
　　获取子进程的进程ID。
Popen.returncode 
　　获取进程的返回值。如果进程还没有结束，返回None。
 下面是一个非常简单的例子，来演示supprocess模块如何与一个控件台应用程序进行交互。
 
import subprocess  
p = subprocess.Popen("app2.exe", stdin = subprocess.PIPE, \  
    stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)   
    p.stdin.write('3\n')  
    p.stdin.write('4\n')  
    print p.stdout.read()  
#---- 结果 ----  
input x:   
input y:   
3 + 4 = 7  
app2.exe也是一个非常简单的控制台程序，它从界面上接收两个数值，执行加操作，并将结果打印到控制台上。代码如下：
 
#include <iostream>  
using namespace std;  
  
int main(int argc, const char *artv[])  
{  
    int x, y;  
    cout << "input x: " << endl;  
    cin >> x;  
    cout << "input y: " << endl;  
    cin >> y;  
    cout << x << " + " << y << " = " << x + y << endl;  
    return 0;  
}  

supprocess模块提供了一些函数，方便我们用于创建进程。
subprocess.call(*popenargs, **kwargs)
　　运行命令。该函数将一直等待到子进程运行结束，并返回进程的returncode。文章一开始的例子就演示了call函数。如果子进程不需要进行交互,就可以使用该函数来创建。
subprocess.check_call(*popenargs, **kwargs) 
　　与subprocess.call(*popenargs, **kwargs)功能一样，只是如果子进程返回的returncode不为0的话，将触发CalledProcessError异常。在异常对象中，包括进程的returncode信息。


'''
