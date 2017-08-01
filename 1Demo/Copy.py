# -*- coding: utf-8 -*-
#8.17. copy — Shallow and deep copy operations
import copy
#浅拷贝

#深拷贝
class MyClass:
    def __init__(self,name):
        self.name = name
    def __cmp__(self,other):
        return cmp(self.name,other.name)
a = MyClass('a')
my_list = [a]
dup = copy.copy(my_list)
print my_list
print dup
print dup is my_list
print dup == my_list
print dup[0] is my_list[0]
print dup[0] == my_list[0]
dup = copy.deepcopy(my_list)
print my_list
print dup
print dup is my_list
print dup == my_list
print dup[0] is my_list[0]
print dup[0] == my_list[0]
