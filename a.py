#!/usr/bin/env python
# encoding: utf-8

class Foo:
    def Bar(self):
        print('Bar')
    def Hello(self, name):
        print('i am %s' %name)

obj = Foo()
obj.Bar()
obj.Hello('Jack')
