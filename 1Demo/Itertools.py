# -*- coding: UTF-8 -*-
from itertools import *
#chain() 处理多个序列而不必构造出一个大列表
for i in chain([1,2,3],['a','b','c']):
    print i
#izip() 返回一个迭代器,而不是列表
for i in izip([1,2,3],['a','b','c']):
    print i
#islice() 返回一个迭代器，它按索引返回由输入迭代器所选的元素
for i in islice(count(),10,20,2):
    print i
#tee() 根据一个源输入迭代器返回多个独立的迭代器（）默认为两个
i1,i2 = tee([1,2,3,4,5])
print list(i1),list(i2)
#imap()
#count()返回一个迭代器，能无限地生成连续整数
for i in count():
    print i
#repeat()返回一个迭代器，每次访问时会生成相同的值
for i in repeat('Hello',5):
    print i
#dropwhile()
#takewhile()
#ifilter()
#ifilterfalse()
#groupby()
