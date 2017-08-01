# -*- coding: utf-8 -*-
import heapq
#创建堆(最小堆)
data = [19,2,32,11,24,9,4,10,11]
h1 = []
for n in data:
    heapq.heappush(h1,n)#依次向堆中添加
h2 = heapq.heapify(data)#原地重新组织列表元素，更高效

#访问堆
h3 = heapq.heappop(h1)#删除最小的元素，并返回删除的值
print h3

h4 = heapq.heapreplace(data,100)#替换堆顶元素为100，并重新排序
#堆的数据极值
print heapq.nsmallest(2,data)
print heapq.nlargest(2,data)
