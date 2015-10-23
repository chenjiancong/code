#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: fun_examples.py
#一些有意思的例子

#计算 1*1+2*2+3*3+...100*100
L = []
x = 1
while x <= 100:
    L.append(x*x)
    x = x + 1
print sum(L)


