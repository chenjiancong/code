#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: python_example.py

print 'ex1:x**n'
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    print s
power(2,10)

print '==========================='

print 'ex2:a**2+b**2+c**2+...'

print '==========================='
print 'ex3:n!=1*2*3*...n'
def fact(n):
    if n == 1:
        return 1
    return  n * fact(n - 1)
print fact(3)

print '==========================='
print 'ex4:[1*1,2*2,3*3,...10*10]'
print [x * x for x in range(1,11)]

print 'other way'
l = []
for x in range(1,11):
    l.append(x*x)
print l

print '==========================='
print '''ex5:ABC','XYZ' ==> 'AX','AY','AZ','BX','BY'...'''
print [m + n for m in 'ABC' for n in 'XYZ']

def aa():
    '''These are some examples
    '''

print aa.__doc__

