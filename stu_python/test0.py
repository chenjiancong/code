#!/usr/bin/env python
# encoding: utf-8

# 求和
def total_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(total_sum(100))

# 求积
def func1(n):
    if n == 1:
        return 1
    return n * func1(n - 1)
print(func1(4))

# 统计 lst = [1,1,2,2,2,3,4,4,4,5] 各数字出现次数
lst = [1,1,2,2,2,3,4,4,4,5]
a = {i:lst.count(i) for i in set(lst)}
print(a)

# wrapper
import time
def my_func(func):
    def wrapper(*args, **kw):
        print('Func is:',func.__name__)
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args, **kw)
    return wrapper

@my_func
def func2(*args):
    s = 0
    for i in args:
        s += i
    return s
print(func2(1,2,3))

# property
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def print_full_name(self):
        print('Full_name:{} {}'.format(self.first_name, self.last_name))

t = Person('M', 'J')
t.print_full_name

