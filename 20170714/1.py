#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-14 16:34:32
# @Author  : Xuliwei (srj520w@gmail.com)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$
print('Hello  World')
print('今天是周五了')

#name=input()
#print(name)
a=100
if a>0:
	print(a)
else:
	print(a+a)
print(10//3)

#list列表
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[-1])
#在list尾追加元素
classmates.append('Adam')
print(classmates)
#在list制定位置添加元素
classmates.insert(1, 'Jack')
# 要删除list末尾的元素，用pop()方法
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop()
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
# list元素也可以是另一个list，比如
s = ['python', 'java', ['asp', 'php'], 'scheme']
# tuple另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
classmate = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
# 要定义一个只有1个元素的tuple,只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
import urllib