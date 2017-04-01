#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
#Filename: for.py

for x in range(1,11):
    print x

    if x == 8:
        pass     #代码桩,起占位作用
    if x == 4:
        print "Hello, 4"
        continue #跳过执行

    if x == 6:
        break    #停止执行
    print "#"*50

    if x == 5:
        exit()   #跳出程序

    print "#"*50

for x in range(1,11):
    print "-------->",x


s = 0
for s in range(1,11):
    s = s + 1
    print s

for s in range(1,11):
    s = s + 1
print s
