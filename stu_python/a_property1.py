#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def print_full_name(self):
        print('{} {}'.format(self.__first_name, self.__last_name))

M = Student('M', 'J')
M.print_full_name
