#!/usr/bin/env python
# encoding: utf-8


def calc(*numbers):
    '''    hello    '''
    sum = 0
    for i in numbers:
        sum = i + i
    return sum

print(calc(1,2))
print(calc.__doc__)
