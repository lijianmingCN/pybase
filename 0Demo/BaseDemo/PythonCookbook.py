# -*- coding: utf-8 -*-
'''
Alist = list(astring)
Newstring = astring.join(bstring)
For s in string:
    pass
result = [do_something_with(c) for c in thestring]
result = map(do_something,thestring)
 
ord('a') à97
chr(97) à’a’
 
判断是够是字符串
Def isASting(anobj):
    Return isinstance(anobj,basestring)
Basestring 是str和unicode的共同基类
 
实现字符串对其
print '|','a'.ljust(20),'|','b'.rjust(20),'|','c'.center(20),'|'
 
删除字符串两端的空格
String.rstrip()
String.lstrip()
String.strip()
 
字符串拼接
1、’’.join(list) #list中的元素一次拼接，无中间过程，效率更高
2、字符串格式化操作符
3、+
 
字符串倒转
切割 string.split()
倒转[::-1] 或reversed()
拼接’’.join()
 
涉及集合问题最好使用内建类型set
 
控制大小写
>>> 'ABC'.lower()
'abc'
>>> 'abc'.upper()
'ABC'
>>> 'abc'.capitalize()
'Abc'
>>> 'ab cd'.title()
'Ab Cd'
 
Unicode
 
文本读取
除非文件巨大，不然一次性读取简单方便
文本写入
字符串列表 用writelines 速度更快
 
Import zipfile
祝你能用‘r’打开，且不能处理分卷和带有注释的zip
 
Import cStringIO
F = CStringIO.StringIO(datastring)
将一串字节封装起来，让你像访问文件对象一样访问其中的数据
 
Import tarfile
 
Windows上修改文件属性
Import win32con，win32api
 
跨平台文件锁2.28
 
十进制速度比float慢得多
Import decimal
>>> decimal.Decimal('1.2')+decimal.Decimal('1.2')
Decimal('2.4')
 
>>> a = ['a','b','c','d','e','f']
>>> for i,j in enumerate(a):
         print i,j
 
创建多维度列表，同时避免隐式引用
列表推到
m = [[0 for col in range(5)] for row in range(10)]




'''