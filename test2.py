#!/usr/bin/env python
# encoding: utf-8

def log(func):
<<<<<<< HEAD
    def wrapper(*args, **kw):
        print('call {}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('Hello')

f = now
f()
=======
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
>>>>>>> b062c8b86d990d916b065823835e4f7a4ae43997
