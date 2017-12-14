#!/usr/bin/env python
# encoding: utf-8

# 求x的n次方
def func1(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(func1(5, 3))

# 在list后加'end'
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end([1, 2]))

def add_end1(*args):
    L = list(args)
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end1('aa'))
