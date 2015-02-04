#!/usr/bin/python
#Filename: lambda.py
#-*- coding:utf-8 -*-

x = int(raw_input('Start Num '))
y = int(raw_input('Stop Num '))

f = reduce(lambda x,y:x*y,range(x,y))
print f
print range(x,y)

#lambda 是匿名函数 lambda x,y:表达式
#reduce 是递归函数
