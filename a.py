#!/usr/bin/env python
# encoding: utf-8

def addEnd(L = None):
    if L == None:
        L = []
    L.append('End')
    return L

def func1(*args):
    L = list(args)
    if L == None:
        L = []
    L.append('End')
    return L

a = func1('aa', 123)
print(a)
