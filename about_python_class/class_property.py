#!/usr/bin/env python
# encoding: utf-8

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.birth = 18
print(s.age)
