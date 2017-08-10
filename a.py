#!/usr/bin/env python
# encoding: utf-8

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1 = count()
