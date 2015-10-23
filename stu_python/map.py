#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: map.py

#map(f,[]) ==> []  输出一个list
s1 = map(lambda x:x*x,range(1,6))
print s1

#reduce(f,()) ==> x 输出的是一个数值
s2 = reduce(lambda x,y:x*y,range(1,6))
print s2
s3 = reduce(lambda x,y:x*10+y,[1,3,5,7,9])
print s3



L1 = ['tom','MeRry','JACK']
l1 = [s.lower() for s in L1]
print l1
print map(lambda s:s[0].upper()+l1[1:].lower(),l1)

i = 'aaaaadfadf'
print i[0].upper()+i[1:].lower()
