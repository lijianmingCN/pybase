# -*- coding: utf-8 -*-
#8.3. collections — High-performance container datatypes
#This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.


'''
class collections.Container 
class collections.Hashable 
class collections.Sized 
class collections.Callable 
ABCs for classes that provide respectively the methods __contains__(), __hash__(), __len__(), and __call__().

class collections.Iterable 
ABC for classes that provide the __iter__() method. See also the definition of iterable.

class collections.Iterator 
ABC for classes that provide the __iter__() and next() methods. See also the definition of iterator.

class collections.Sequence 
class collections.MutableSequence 
ABCs for read-only and mutable sequences.

class collections.Set 
class collections.MutableSet 
ABCs for read-only and mutable sets.

class collections.Mapping 
class collections.MutableMapping 
ABCs for read-only and mutable mappings.

class collections.MappingView 
class collections.ItemsView 
class collections.KeysView 
class collections.ValuesView 
'''



from collections import Counter
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    c[word] += 1
print c
print 'elements counts:',c['red']
print 'the n most common elements and their counts:',c.most_common(2)
print c.copy()
print sum(c.values())
print list(c.elements())
print set(c)
print list(c)
print dict(c) 
print c.items()
print c.most_common()[:-3:-1] #n least common elements
c.clear()

a = Counter(a=4, b=2, c=0, d=-2)
b = Counter(a=1, b=2, c=3, d=4)
print a + b
print a - b
print a & b
print a | b
a.subtract(b)
print a

    
    
#容器counter，可以跟踪相同的值增加了多少次，可以用来实现包或多集合
#初始化
A = Counter(['a','b','c','a','b','b'])
B = Counter({'a':2,'b':3,'c':1})
C = Counter(a=2,b=3,c=1)
C.update('dddd')
C.update(e=10)
#访问计数
print C['a']#获取'a'的个数
print list(C.elements())#elements()返回一个迭代器,生成Counter中的所有元素
print C.most_common(3)#most_common()生成一个序列，其中包含n个最常遇到的输入值及其相应计数
#算数操作
C1 = Counter(a=3,b=3,c=3)
C2 = Counter(a=1,b=1,c=1,d=2,e=2)
print C1+C2#合并
print C1-C2#C1比C2多的部分
print C1&C2#交集，共有部分
print C1|C2#并集，集成两集合最大部分