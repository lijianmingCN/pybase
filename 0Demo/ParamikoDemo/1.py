# -*- coding: cp936 -*-
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.104.6.8',username = 'xiaopeng',password='******')
cmd = 'cd'    #�����û�Ŀ¼home
stdin,stdout,stderr = ssh.exec_command(cmd)
cmd = 'ls >test'  #�ܵ���ls������������ļ�test����
stdin,stdout,stderr = ssh.exec_command(cmd)
cmd = 'cat test'  # ��ʾtest�����ݣ���ls�����Ľ��
stdin,stdout,stderr = ssh.exec_command(cmd)
print stdout.readlines()   #��� �����õ��ַ���ʾ
['code\n', 'Desktop\n', 'order.cpp\n', 'python\n', 'test\n', '\xe5\x85\xac\xe5\x85\xb1\xe7\x9a\x84\n', '\xe6\xa8\xa1\xe6\x9d\xbf\n', '\xe8\xa7\x86\xe9\xa2\x91\n', '\xe5\x9b\xbe\xe7\x89\x87\n', '\xe6\x96\x87\xe6\xa1\xa3\n', '\xe4\xb8\x8b\xe8\xbd\xbd\n', '\xe9\x9f\xb3\xe4\xb9\x90\n']
�������Ƕ��ᷢ�֣�ʹ��exec_command('cd dirname')ʱ�������л�Ŀ¼��execute_command() ��a single session��ÿ��ִ�����Ҫ�ص�ȱʡĿ¼�����Կ��� .execute_command('cd  /var; pwd')��
ssh.close()
