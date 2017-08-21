#!/usr/bin/env python
# encoding: utf-8

def func1(*args):
    L = list(args)
    if args == None:
        L = []
    L.append('End')
    return L

print(func1())

L1 = ['tom', 'peter']
def toUpper(L1):
    return L1.upper()

a = map(toUpper, L1)
print(list(a))
