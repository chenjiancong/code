#!/usr/bin/env python
# encoding: utf-8
# 类属性

class Student(object):
    name = 'GZ_school'

    def __init__(self, name):
        self.name = name

s = Student('tom')
print(s.name)
print(Student.name)

