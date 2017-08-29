#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

#    def print_name(self):
#        print('{}:{}'.format(self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score = score

tom = Student('Tom', 80)
print(tom.get_name())
