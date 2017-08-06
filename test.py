#!/usr/bin/env python
# encoding: utf-8

class Foo:
    def __init__(self, name, age, genter):
        self.name   = name
        self.age    = age
        self.genter = genter

    def kanchai(self):
        print('{name}, {age}岁,{genter}, 上山去砍柴'
                .format(name = self.name, age = self.age, genter = self.genter)
             )

xiaoming = Foo('xiaoming', 10, '男')
xiaoming.kanchai()

class Animal:
    def eat(self):
        print('{} 吃'.format(self.name))

class Cat(Animal):
        def __init__(self, name):
            self.name = name

c1 = Cat('小花gay')
c1.eat()
