# -*- coding: utf-8 -*-
#8.6. array — Efficient arrays of numeric values
#This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers.
import array

i = array.array('i',xrange(5))
c = array.array('c','hello world')
u = array.array('u', u'hello world')
l = array.array('l', [1, 2, 3, 4, 5])
d = array.array('d', [1.0, 2.0, 3.14])

print 'i:',i
print 'typecode:',c.typecode
print 'itemsize:',l.itemsize
d.append(6)#追加
print 'append double:',d
d.extend([7,8,9])
print 'extned bouble',d
print 'memory address and the length:',l.buffer_info()
print 'the number of occurrences of x in the array:',l.count(3)
print 'the number of index of x in the array:',d.index(3.14)
c.insert(0, '!')#insert element
print 'new array:',c
c.pop(0)
print 'new array:',c
print 'Slice:',d[2:5]#切片
print 'Iterator:',list(enumerate(d))#遍历







