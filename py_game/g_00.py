#!/usr/bin/env python
# encoding: utf-8

# 1,2,3,4 组合成无重复3位数
#for x in range(100, 500, 100):
#    for y in range(10, 50, 10):
#        for z in range(1, 5):
#            print(filter(x + y + z))

def func(n):
    n <= 10
g = [a * 1 for a in range(1, 444)]
a = filter(func, g)
print(list(a))
#x = [a * 1 for a in range(1, 5)]
#y = [b * 10 for b in range(1, 5)]
#z = [c * 100 for c in range(1, 5)]
#print(x, y, z)

