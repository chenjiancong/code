#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: list&tuple.py

#-------About List-------
#list 是有序集体,能增删其中元素

L = ['a1','a2','a3','a4']

#-------显示-------
print L
print 'L[0] =>',L[0]
print 'L[-1] =>',L[-1]

#-------添加元素-------
#append(),追加到元素末尾
#L.append('a5')
#insert(),插入到指定位置
#L.insert(0,'a0')

#-------删除元素-------
#pop(),删除元素最后一位,亦可从右往左指定删除
L = ['a1','a2','a3','a4']
#Example,删除‘a3’
#L.pop(2)

#-------替换元素-------
#将'a2'替换成‘A2’
#L[2] = 'A2'


#-------About Tuple-------
#一但创建不能修改
#0个元素和1个元素的区别
#t = () 表示空的tuple
#t = (1,) 表示1个元素的tuple


#-------About Dict-------
#dict特点:
#1,查找速度快,但占用内存大(list正好与之相反)
#2,存储key-value是无顺序的(list有顺序)
#3,key元素必须不可变

dict = {'A':90,'B':80,'C':70,'D':60}
#访问字典元素
#get()
print dict.get('D')
print dict.get('E')

#添加元素&修改元素
dict['Z'] = 10
dict['D'] = 59

#  删除字典元素
del dict['D']

#遍历dict的key
for key in dict:
    print key

#-------About Set-------
#1,set元素是无序且不重复
#2,元素不可变
#3,set与dict很似,唯一区别是不存储value,因此判断元素是否在set很快

#显示set(['A','B','C','D'])
s = set(['A','B','C','C','D'])
print s

#访问set
#set不能通过索引来访问,只能判断元素是否在set中
#如判断'E'是否在s中
print 'E' in s
print 'A' in s

#判断元素是否在set里
x = 'WED'
weekdays = set(['MON','TUE','WED','THU','FRI','SAT','SUN'])
if x in weekdays:
    print 'input right'
else:
    print 'input wrong'

#添加&删除元素
s2 = set(['A','B','C'])
s2.add('Y')            #无论Y是否在元素里,都增加进去
s2.remove('G')         #先判断G是否在元素里,再删除
