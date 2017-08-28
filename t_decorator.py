#!/usr/bin/env python
# encoding: utf-8

from functools import reduce

def log(func):
    def wrapper(*args, **kw):
        print('Call: {}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def func1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(func1(4))

@log
def func1(n1):
    def func2(n2):
        print('number2:{}'.format(n2))
        return n1 + n2
    return func2
n = func1(10)
print(n(20))

@log
def func1(n):
    return reduce(lambda x, y: x + y, range(1, n + 1))
print(func1(100))
