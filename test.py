#!/usr/bin/env python
# encoding: utf-8

def worker(a, b, c):
    x = a + b
    y = x * c
    return y

result = worker(1, 2, 3)
print(result)

