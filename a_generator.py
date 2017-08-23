#!/usr/bin/env python
# encoding: utf-8

def func(n):
    for i in range(n + 1):
        yield i

g = func(4)
print(type(g))

for i in g:
    print(i)
