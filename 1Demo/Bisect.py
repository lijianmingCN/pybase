# -*- coding: utf-8 -*-
#8.5. bisect — Array bisection algorithm
#维护有序列表，向列表添加元素后不必sort排序
import bisect

data = [1,3,3,6,8,12,15]
bisect.insort(data,3)#其插入的结果是不会影响原有的排序。
print data
print bisect.bisect(data,1)#查找该数值将会插入的位置并返回，而不会插入。
print bisect.bisect_left(data,3)#在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回左侧位置１
print bisect.bisect_right(data,3)#在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回右侧位置３
bisect.insort_left(data,3)#将x插入到列表L中，x存在时插入在左侧
bisect.insort_right(data,3)#将x插入到列表L中，x存在时插入在右侧
print data