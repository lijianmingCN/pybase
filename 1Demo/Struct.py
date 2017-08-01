# -*- coding: utf-8 -*-
'''struct中支持的格式如下表：
Format C_Type Python 字节数
x pad byte no value 1 
c char string of length 1 1 
b signed char integer 1 
B unsigned char integer 1 
? _Bool bool 1 
h short integer 2 
H unsigned short integer 2 
i int integer 4 
I unsigned int integer or long 4 
l long integer 4 
L unsigned long long 4 
q longlong long 8 
Q unsigned long long long 8 
f float float 4 
d double float 8 
s char[] string 1 
p char[] string 1 
#P void* long 
注1.q和Q只在机器支持64位操作时有意思
注2.每个格式前可以有一个数字，表示个数
注3.s格式表示一定长度的字符串，4s表示长度为4的字符串，但是p表示的是pascal字符串
注4.P用来转换一个指针，其长度和机器字长相关
注5.最后一个可以用来表示指针类型的，占4个字节
为了同c中的结构体交换数据，还要考虑有的c或c++编译器使用了字节对齐，通常是以4个字节为单位的32位系统，
故而struct根据本地机器字节顺序转换.可以用格式中的第一个字符来改变对齐方式.定义如下：
Character Byte order Size and alignment
@ native native            凑够4个字节 
= native standard        按原字节数 
< little-endian standard        按原字节数 
> big-endian standard       按原字节数 
! network (= big-endian) 
standard       按原字节数
使用方法是放在fmt的第一个位置，就像'@5s6sif'
'''
import struct
a=20
b=400
c='A'
str=struct.pack('2ic',a,b,c)#转换成字节流，虽然还是字符串，但是可以在网络上传输
print 'len:',len(str)               #2i 表示两个int
a1,a2,a3=struct.unpack('2ic',str)
print 'unpack:',a1,a2,a3
print 'size:',struct.calcsize('HH4s')#用来计算特定格式的输出的大小，是几个字节

#利用缓冲区
import struct
import binascii
import ctypes
values = (1, 'abc', 2.7)
s = struct.Struct('I3sf')
prebuffer = ctypes.create_string_buffer(s.size)
print 'Before :',binascii.hexlify(prebuffer)
s.pack_into(prebuffer,0,*values)
print 'After pack:',binascii.hexlify(prebuffer)
unpacked = s.unpack_from(prebuffer,0)
print 'After unpack:',unpacked
'''对比使用pack方法打包，pack_into 方法一直是在对prebuffer对象进行操作，没有产生多余的内存浪费。
另外需要注意的一点是，pack_into和unpack_from方法均是对string buffer对象进行操作，
并提供了offset参数，用户可以通过指定相应的offset，使相应的处理变得更加灵活。
例如，我们可以把多个对象pack到一个buffer里面，然后通过指定不同的offset进行unpack：'''

import struct
import binascii
import ctypes
values1 = (1, 'abc', 2.7)
values2 = ('defg',101)
s1 = struct.Struct('I3sf')
s2 = struct.Struct('4sI')
prebuffer = ctypes.create_string_buffer(s1.size+s2.size)
print 'Before :',binascii.hexlify(prebuffer)
s1.pack_into(prebuffer,0,*values1)
s2.pack_into(prebuffer,s1.size,*values2)
print 'After pack:',binascii.hexlify(prebuffer)
print s1.unpack_from(prebuffer,0)
print s2.unpack_from(prebuffer,s1.size)



