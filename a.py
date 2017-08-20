#!/usr/bin/env python
# encoding: utf-8

def addEnd(L = None):
    if L == None:
        L = []
    L.append('End')
    return L

a=addEnd([])
print(a)

def gensquares(n):
    for i in range(n):
        yield i ** 2

for item in gensquares(5):
    print(item)
