#!/usr/bin/env python
# encoding: utf-8

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

import time

date = input('输入年月日(eg 2017/09/12): ')
print('strftime(%Y/%m%d)'.format(time.now()))
