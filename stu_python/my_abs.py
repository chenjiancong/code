#!/usr/bin/env python
# encoding: utf-8

def my_abs(x):
    if not isinstance(x(int, float)):
        raise TypeError('Bad Operand Type ')

    if x >=0:
        return x
    else:
        return -x
print my_abs('a')
print my_abs(10)
print my_abs(-4)

