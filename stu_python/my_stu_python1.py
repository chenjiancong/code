#!/usr/bin/env python
# encoding: utf-8

# 一些练习题

# 累加1+2+3+...


def func0(n):
    s, i = 0, 1
    while n >= i:
        s += i
        i += 1
    return s


print(func0(100))


# 使用 reduce
from functools import reduce


def func1(n):
    s = reduce(lambda x, y: x + y, range(1, n + 1))
    return s


print(func1(100))

# 求积 1*2*3*...


def func2(n):
    s = reduce(lambda x, y: x * y, range(1, n + 1))
    return s


print(func2(4))


def func3(n):
    if n == 1:
        return 1
    return n * func3(n - 1)


print(func3(5))

# 求n的x次方


def func(n, x):
    s = pow(n, x)
    return s


print(func(2, 10))


def func11(n, x=2):
    s = 1
    while x > 0:
        s = s * n
        x = x - 1
    return s


print('n的x次方', func11(2, 10))

# wrapper 使用


def my_func(func):
    def wrapper(*args, **kw):
        print('Func is:', func.__name__)
        return func(*args, **kw)
    return wrapper


@my_func
def func4():
    print('Hello World')


func4()

# 使用time
import time
print('Now is ', time.strftime('%Y-%m-d %H:%M:%S'))
