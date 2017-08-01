# -*- coding: utf-8 -*-
import random
#random.seed(1000)
print random.random()#0到1的随机符点数
print random.randint(1, 10)#指定范围内的整数
print random.randrange(0, 101, 2)#随机选取0到100间的偶数
print random.uniform(10, 20)#指定范围内的随机符点数
print random.choice("ABCDEFG")#从序列中获取一个随机元素
print random.choice(["JGood", "is", "a", "handsome", "boy"])
print random.choice(("Tuple", "List", "Dict"))
print random.sample('abcdefghij', 3)#多个字符中选取特定数量的字符
p = ["Python", "is", "powerful", "simple", "and so on..."]
random.shuffle(p)#将一个列表中的元素打乱
print p

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(l, 5)  # 从list中随机获取5个元素，作为一个片断返回
print slice
print l  # 原有序列并没有改变