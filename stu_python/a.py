#!/usr/bin/env python
# encoding: utf-8

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print sum

sum = 0
for x in range(1,101,2):
    sum = sum + x
print sum

a = 99
while a > 0:
    a = a -2
print a

num = int(raw_input('enter num:'))
print num


s = set([1,num,3])
print s
