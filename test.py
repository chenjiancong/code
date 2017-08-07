#!/usr/bin/env python
# encoding: utf-8

<<<<<<< HEAD
# 封装
class Foo:
    def __init__(self, name, age, gender):
        self.name = name
        self.age  = age
        self.gender  = gender

    def kanchai(self):
        print('{0},{1},{2}, 上山去砍柴' .format(self.name,self.age,self.gender))

xiaoming = Foo('小明', 10, '男')
xiaoming.kanchai()

# 继承
class Animal:
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
=======
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
>>>>>>> dd270fb97fea2d5161417be680ef66022fbea70e
