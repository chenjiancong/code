#!/usr/bin/env python
# encoding: utf-8

# 递归
def func0(x):
    if x == 1:
        return x
    return x * func0(x - 1)
print(func0(5))

# 100 以内的奇数有哪些
99, 97, 95
