#!/usr/bin/env python
# encoding: utf-8

def func1(*args):
    def func2(number):
        sum = 0
        for i in args:
            sum += i
    return func2

n = func1(1,2)
print(n())

