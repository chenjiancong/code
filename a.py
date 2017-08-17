#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    school = 'GZ_School'
    def f(self):
        return '你好'

t = Student()
print(t.school)
print(t.f())
