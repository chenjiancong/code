#!/usr/bin/env python
# encoding: utf-8

class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(animal):
        animal.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
#dog.run()
dog.run_twice()

cat = Cat()
cat.run_twice()
