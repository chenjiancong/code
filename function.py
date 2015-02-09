#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: function.py

L = ['Arb','tom','mErry','jacK']

print '=#===l1===='
l1 = [s.lower() for s in L]
print l1

print '====l2===='
for l2 in l1:
    print l2

:
print l1[0][0].upper()+l1[0][1:].lower()
