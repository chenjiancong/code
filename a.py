#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    school = 'GZ_School'
    def f(self):
        return 'hello'

t = Student()
print(t.school)
print(t.f())
