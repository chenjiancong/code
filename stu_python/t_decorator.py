#!/usr/bin/env python
# encoding: utf-8

from functools import reduce

def log(func):
<<<<<<< HEAD
    def wrapper(*args, **kw):
        print('Call: {}'.format(func.__name__))
=======
    def warrper(*args, **kw):
        print('函数名: {}'.format(func.__name__))
        print('参数： {}'.format(func))
>>>>>>> 26346d661745d30828b8061028fff810477901fc
        return func(*args, **kw)
    return warrper
@log
<<<<<<< HEAD
=======
# 阶乘
>>>>>>> 26346d661745d30828b8061028fff810477901fc
def func1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(func1(4))

<<<<<<< HEAD
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
=======
>>>>>>> 26346d661745d30828b8061028fff810477901fc
