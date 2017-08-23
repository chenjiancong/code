#!/usr/bin/env python
# encoding: utf-8

from functools import reduce

# 阶乘1
def func1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(func1(4))

def func11(n):
    if n == 1:
        return 1
    return n * func11(n - 1)
print(func11(4))


# 求和1
def func2(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum
print(func2(100))

def func3(n):
    sum = 0
    i = 1
    while n - i >= 0:
        sum += i
        i += 1
    return sum
print(func3(100))
