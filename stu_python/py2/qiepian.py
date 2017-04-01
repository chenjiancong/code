#!/usr/bin/env python
# encoding: utf-8

d={'a':1, 'b':3, 'c':5}
for key in d:
    print key

for v in d.itervalues():
    print v

for k, v in d.items():
    print k,v
