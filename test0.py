#!/usr/bin/env python
# encoding: utf-8

def my_func(func):
    def wrapper(*args, **kw):
        print('Func is:{}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@my_func
def cal_sum(*args):
    s = 0
    for i in args:
        s = s + i
    return s

print(cal_sum(1,3))
