#!/usr/bin/env python
# encoding: utf-8

from functools import reduce

def log(func):
    def wrapper(*args, **kw):
        print('{}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def func3(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(func3(4))
