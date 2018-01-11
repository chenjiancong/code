#!/usr/bin/env python
# encoding: utf-8

<<<<<<< HEAD
def add_end(L = None):
    if L is None:
        L = []
        L.append('END')
    return L

add_end('123')
print(L)
=======
def add_end(L=[]):
    L.append('END')
    return L

l = add_end([1,2])
print(l)
>>>>>>> 53ffc4e64fe1660194ca858c0ca1892c9ebb1c53
