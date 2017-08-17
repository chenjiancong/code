#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    school = 'GZ_School'

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def detial(self):
        print('Student name:{}'.format(self.name))

tom = Student('Tom', 18)
print(tom.school)
tom.detial()
