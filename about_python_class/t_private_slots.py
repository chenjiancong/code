#!/usr/bin/env python
# encoding: utf-8

# private
class Student(object):
    # __slots__
    __slots__ = ('name', 'score')
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


s = Student('tom', 80)
print(s.get_name())
s.set_score = 99
print(s.get_score())
