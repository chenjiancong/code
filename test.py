#!/usr/bin/python
#-*- coding:utf-8 -*-

#for x in range(1,20,3):
#    print x

print reduce(lambda x,y:x+y,range(1,101,3))
print range(1,101,3)
print reduce(lambda x,y:x+y,range(1,101,3))
