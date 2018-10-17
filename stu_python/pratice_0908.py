#!/usr/bin/env python
# encoding: utf-8

from functools import reduce

# 1+2+3+...
def fun1(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum
a = fun1(100)
print(a)

def func11(n):
    sum = 0
    i = 1
    while n - i >= 0:
        sum = sum + i
        i = i + 1
    return sum
aa11 = func11(100)
print(aa11)

# 4*3*2*1
def func2(n):
    if n == 1:
        return 1
    return n * func2(n - 1)
b = func2(4)
print(b)

def func3(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
c = func3(4)
print(c)

# add 'end'
def AddEnd(*args):
    L = list(args)
    if args == None:
        L = []
    L.append('End')
    return L
a1 = AddEnd(1,2,3)
print(a1)

# @uid
def uid(func):
    def warrper(*args, **kw):
        print('UID:222')
        return func(*args, **kw)
    return warrper

@uid
def Hello(args):
    print('Hello, {}'.format(args))
Hello('123')
