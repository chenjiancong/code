#!/usr/bin/env python
# encoding: utf-8

class Foo(object):
    def __init__(self, name):
        self.name = name

    def Hello(self):
        print('hello,{}'.format(self.name))

obj = Foo('tom')
obj.Hello()
