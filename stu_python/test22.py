#!/usr/bin/env python
# encoding: utf-8

# x的n次方
def func(x, n = 2):
    '''
    定义 s = 1
    '''
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print(func(4))
print(func.__doc__)
