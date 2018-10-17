#!/usr/bin/env python
# encoding: utf-8


def pi_sum(n):
#    sum = 0
#    i   = 1
    sum, i = 0, 1
    while n - i >= 0:
        sum = sum + 8 / (i * (i + 2))
        i   = i + 4
    return sum

print(pi_sum(100))
