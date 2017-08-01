# -*- coding: cp936 -*-
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.104.6.8',username = 'xiaopeng',password='******')
cmd = 'cd'    #进入用户目录home
stdin,stdout,stderr = ssh.exec_command(cmd)
cmd = 'ls >test'  #管道，ls命名的输出到文件test里面
stdin,stdout,stderr = ssh.exec_command(cmd)
cmd = 'cat test'  # 显示test的内容，即ls命名的结果
stdin,stdout,stderr = ssh.exec_command(cmd)
print stdout.readlines()   #结果 汉字用的字符显示
['code\n', 'Desktop\n', 'order.cpp\n', 'python\n', 'test\n', '\xe5\x85\xac\xe5\x85\xb1\xe7\x9a\x84\n', '\xe6\xa8\xa1\xe6\x9d\xbf\n', '\xe8\xa7\x86\xe9\xa2\x91\n', '\xe5\x9b\xbe\xe7\x89\x87\n', '\xe6\x96\x87\xe6\xa1\xa3\n', '\xe4\xb8\x8b\xe8\xbd\xbd\n', '\xe9\x9f\xb3\xe4\xb9\x90\n']
这里我们都会发现，使用exec_command('cd dirname')时并不会切换目录，execute_command() 是a single session，每次执行完后都要回到缺省目录。所以可以 .execute_command('cd  /var; pwd')。
ssh.close()
