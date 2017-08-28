#!/usr/bin/env python
# encoding: utf-8

<<<<<<< HEAD
def log(func):
    def wrapper(*args, **kw):
        print('call {}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('Hello')

f = now
f()
    def wrapper(*arg, **kw):
        print('{}'.format(func.__name__))
        return func(*arg, **kw)
    return wrapper

@log
def func1():
    print('Hello')

@log
def func2():
    print('AA')

a = func1
a()

func2()
=======
from functools import reduce

def func1(n):
    sum = 0
    for i in range(n + 1):
        return sum = sum + i
    return sum
print(func1(100))
>>>>>>> 26346d661745d30828b8061028fff810477901fc
