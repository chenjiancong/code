#!/usr/bin/env python
# encoding: utf-8

L = ['tom','jack']
def toUpper(L):
    return L.upper()

def toTitle(L):
    return L.title()

#map(toUpper,L)
#print(list(map(toUpper,L)))

a = list(map(toUpper, L))
print(a)

print(list(map(toTitle, L)))
