#!/usr/bin/env python
# encoding: utf-8

from functools import reduce

def log(func):
    def warrper(*args, **kw):
        print('函数名: {}'.format(func.__name__))
        print('参数： {}'.format(func))
        return func(*args, **kw)
    return warrper
@log
# 阶乘
def func1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(func1(4))

