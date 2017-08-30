#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    school = 'GZ_School'
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError('bad score')


tom = Student('tom', 88)
print(tom.get_name())
tom.set_score(10)
print(tom.get_score())
print(tom.school)
