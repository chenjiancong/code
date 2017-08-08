#!/usr/bin/env python
# encoding: utf-8

# 封装
class Foo(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age  = age
        self.gender  = gender

    def kanchai(self):
        print('{0},{1},{2}, 上山去砍柴' .format(self.name,self.age,self.gender))

xiaoming = Foo('小明', 10, '男')
xiaoming.kanchai()

# 继承
class Animal(object):
    def eat(self):
        print('%s 吃'%self.name)
    def drint(self):
        print('%s 喝'%self.name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('喵喵叫')

c1 = Cat('小花猫')
c1.eat()
c1.cry()

