#!/usr/bin/env python
# encoding: utf-8

def log(func):
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
