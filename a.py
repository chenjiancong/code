#!/usr/bin/env python
# encoding: utf-8

def func1(*args):
    L = list(args)
    if args == None:
        L = []
    L.append('End')
    return L

