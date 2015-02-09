#!/usr/bin/python
#Filename: list.py
#-*- coding:utf-8 -*-

L = []    #create none list
n = 1

while n<=99:
    L.append(n)
    n = n + 2

print L

<<<<<<< HEAD
a = [m + n for m in "ABC" for n in "XYZ"]
print a


l1 = ['World','EMS',1111,'Lenovo','OK']
s = [s.lower() for s in l1]
print s

s1 = [s.lower() for s in l1 if isinstance(s,str) == True]
#s1 = [isinstance(s.lower() for s in l1,str)]
print s1












=======
s1 = [m + n for m in "ABC" for n in "XYZ"]
print s1

l1 = ["AAA",'IBM',"EMS"]
s2 = [s.lower() for s in l1]
print s2
>>>>>>> 0bbf694da24b37a12203bc473bbf0a57fecd7be2
