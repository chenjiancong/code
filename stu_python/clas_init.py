#!/usr/bin/env python
# encoding: utf-8


class Person(object):
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Hello, my name is', self.name)


p = Person('Jack')
p.sayHi()
