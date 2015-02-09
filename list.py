#!/usr/bin/python
#Filename: list.py
#-*- coding:utf-8 -*-

L = []    #create none list
n = 1

while n<=99:
    L.append(n)
    n = n + 2

print L

s1 = [m + n for m in "ABC" for n in "XYZ"]
print s1

l1 = ["AAA",'IBM',"EMS"]
s2 = [s.lower() for s in l1]
print s2
