#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('{name}:{score}'.format(name = self.__name, score = self.__score))

    def print_grade(self):
        if self.__score >= 85:
            print('A')
        elif 70<= self.__score < 85:
            print('B')
        else:
            print('C')

bob = Student('Bob', 4)
bob.print_score()
bob.print_grade()
