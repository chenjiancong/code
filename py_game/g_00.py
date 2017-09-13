#!/usr/bin/env python
# encoding: utf-8

# 1,2,3,4 能组成多少个无重复3位数? 分别是哪些？
res = []
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if x !=y and y != z and x != z:
                res.append(x * 100 + y * 10 + z)
print(len(res))
print(res)
