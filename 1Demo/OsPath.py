# -*- coding: utf-8 -*-
import os
print os.sep #路径分隔符
print os.extsep #扩展名分隔符
print os.pardir #路径中表示目录树上一级的部分（例如:..）
print os.curdir #路径中只是当前目录的部分（例如：.）

filename = "opt/java/bin/java.exe"
print "split", "=>", os.path.split(filename)#文件路径，文件名
print "dirname", "=>", os.path.dirname(filename)#路径
print "basename", "=>", os.path.basename(filename)#文件名
print "splitext", "=>", os.path.splitext(filename)#按照扩展名分割
path = os.path.join(os.path.dirname(filename),os.path.basename(filename))#建立路径
print "join", "=>", path
print os.path.normpath(path)#清楚多余分隔符或相对路径部分
print os.path.exists(filename) 
print os.path.exists('/root') 
print os.path.exists('/root/wc.py')
print os.path.isdir('/root/wc.py')      
print os.path.isdir('/root')      
print os.path.isfile('/root')   
print os.path.isfile('/root/wc.py')  
print os.path.islink('/root/wc.py')#是否是连接文件
print os.path.ismount('/root/wc.py') #是否是挂载文件
#print os.path.getsize('/root/pathdir1') #获取文件（文件夹）大小
#print os.path.getctime('/root/pathdir1/person.py')#创建时间
#print os.path.getmtime('/root/pathdir1/person.py')#修改时间    
#print os.path.getatime('/root/pathdir1/person.py')#访问时间

for root, dirs, files in os.walk('C:/Python27'):
   print root,dirs,files



os.stat(path).st_mtime


