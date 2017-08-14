#!/usr/bin/env python
# encoding: utf-8

def log(func):
    def wrapper(*args, **kw):
        print('call {}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-08-12')

f = now
f()
