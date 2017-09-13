#!/usr/bin/env python
# encoding: utf-8

'''
题目:输入三个整数 x,y,z,请把这三个数由小到大输出。
'''

x = int(input('输入X： '))
y = int(input('输入Y： '))
z = int(input('输入Z： '))

args = x, y, z
L = list(args)
print('由大到小排列', sorted(L, reverse = True))
print('由小到大排列', sorted(L))
print('L的类型', type(L))


