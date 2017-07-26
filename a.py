#!/usr/bin/env python
# encoding: utf-8

def calc(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(calc(1,2))
