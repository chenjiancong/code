#!/usr/bin/env python
# encoding: utf-8

# 累加
def func0(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum

def func1(n):
    sum, i = 0, 1
    while n >= i:
        sum = sum + i
        i = i + 1
    return sum

print(func0(100),func1(100))

# 阶乘
def func2(n):
    if n == 1:
        return 1
    return n * func2(n - 1)
print(func2(5))

# x的n次方
def func3(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print(func3(2, 10))

# 在list后加end
def func4(*args):
    L = list(args)
    if args == None:
        L = []
    L.append('end')
    return L
print(func4('123',123))

# wrapper
def my_func(func):
    def p_name(*args, **kw):
        print('Func is: {}'.format(func.__name__))
        return func(*args, **kw)
    return p_name

@my_func
def cal_sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(cal_sum(1,9))



