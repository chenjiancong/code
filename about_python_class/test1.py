#!/usr/bin/env python
# encoding: utf-8
# 类的多态

class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(animal):
        animal.run()
        animal.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

dog = Dog()
#dog.run()
dog.run_twice()

cat = Cat()
cat.run_twice()

tortoise = Tortoise()
tortoise.run_twice()
