#!/usr/bin/env python
# encoding: utf-8


def func0(n):
    sum, i = 0, 1
    while n >= i:
        sum = sum + i
        i = i + 1
    return sum
print(func0(100))

def func1(n):
    sum, i = 0, 1
    while n >= i:
        i = i + 1
        sum = sum + i
    return sum
print(func1(2))

