#!/usr/bin/env python
# encoding: utf-8

class Person:
    def sayHi(self):
        print 'Hello, how are you?'

#  p = Person()
Person().sayHi()


print 'Hi this is {name}\'s computer'.format(name='jack')

b = "www.baidu.com"
print b.split(".")

a = [1,2,3,4,1,1,22]
print a.count(2)
print a.index(3)
