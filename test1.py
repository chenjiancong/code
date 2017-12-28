#!/usr/bin/env python
# encoding: utf-8

def logging(level):
    def my_func(func):
        def p_name(*args, **kw):
            print('Level is: {level} and Func call: {func}()'.format(
                level = level,
                func = func.__name__)
                    )
            return func(*args, **kw)
        return p_name
    return my_func

def my_func(func):
    def p_name(*args, **kw):
        print('Func is:{}'.format(func.__name__))
        return func(*args, **kw)
    return p_name

#@my_func
@logging(level='Info')
def cal_sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(cal_sum(1,9))
