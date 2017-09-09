#!/usr/bin/env python
# encoding: utf-8

from functools import reduce
# 1+2+3+...
def func (n):
	sum = 0
	for i in range (n + 1):
		sum += i
	return sum

print(func(100))

# 4*3*2*1
def func1 (n):
	return reduce (lambda x, y: x * y, range (1, n + 1))

print(func1(4))
