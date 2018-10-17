#!/usr/bin/env python
# encoding: utf-8

d = {'Tom':90,'Merry':76,'Jack':69}

for name, values in d.iteritems():
    print name, values

for values in d.values():
    print values
