# -*- coding:utf-8 -*-
'''
介绍Cmd一些常用的方法：
（1）cmdloop()：类似与Tkinter的mainloop，运行Cmd解析器；
（2）onecmd(str)：读取输入，并进行处理，通常不需要重载该函数，而是使用更加具体的do_command来执行特定的命名；
（3）emptyline()：当输入空行时调用该方法；
（4）default(line)：当无法识别输入的command时调用该方法；
（5）completedefault(text,line,begidx,endidx):如果不存在针对的complete_*()方法，那么会调用该函数
（6）precmd(line)：命令line解析之前被调用该方法；
（7）postcmd(stop，line)：命令line解析之后被调用该方法；
（8）preloop()：cmdloop()运行之前调用该方法；
（9）postloop()：cmdloop()退出之后调用该方法；
'''
import cmd
import sys

class CmdTest(cmd.Cmd):

    def __init__(self):            #初始基础类方法
        cmd.Cmd.__init__(self)

    def help_hello(self):
        print("输入hello 参数，将执行o_hello方法，输出参数值")

    def do_hello(self,line):
        print("do_hello:",line)

    def help_exit(self):          #以help_*开头的为帮助
        print("输入exit退出程序")

    def do_exit(self,line):       #以do_*开头为命令
        print("Exit:",line)
        sys.exit()

if __name__ =="__main__":
    cmd=CmdTest()
    cmd.cmdloop()
