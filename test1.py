#!/usr/bin/env python
# encoding: utf-8

x = [1, 2, 3]
y = [4, 5, 6]
#n = list(zip(x, y))
# print(n)
#m = list(zip(*n))
# print(m)
# print(type(m))

keys = ['tom', 'jack', 'merry']
vals = [14, 15, 13]
m = list(zip(keys, vals))
print(m)

D2 = {}
for (k, v) in zip(keys, vals):
    D2[k] = v
print(D2)

D3 = dict(zip(keys, vals))
print(D3)

s='abc'
for i in enumerate(s):
    print(i)
