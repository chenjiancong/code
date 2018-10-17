#!/usr/bin/env python
# encoding: utf-8

def func1(m):
    if 0 <= m <= 100:
        print('right')
    else:
        raise ERROR

func1(-111)
