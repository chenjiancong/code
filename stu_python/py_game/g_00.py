#!/usr/bin/env python
# encoding: utf-8

'''
题目:有 1、2、3、4 个数字,能组成多少个互不相同且无重复数字的三位数?都是多少?
'''
res = []
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if x != y and y != x and x != z and y != z:
                res.append(x * 100 + y * 10 + z)

print('总共有{}位'.format(len(res)))
print(res)
