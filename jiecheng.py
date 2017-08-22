#!/usr/bin/env python
# encoding: utf-8

from functools import reduce
# 阶乘1
def f(n):
    return reduce(lambda x, y: x * y,range(1, n + 1))

print(f(4))

# 阶乘2
def f1(n):
    if n == 1:
        return 1
    return n * f(n - 1)

print(f1(4))

# 求和1
def fun1(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(fun1(100))

# 求和2
def func2(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum

print(func2(100))

def func3(n):
    sum = 0
    i = 1
    while n - i >= 0:
        sum = sum + i
        i = i + 1
    return sum

print(func3(100))
