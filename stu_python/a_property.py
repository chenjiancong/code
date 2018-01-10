#!/usr/bin/env python
# encoding: utf-8

class Person(object):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def print_full_name(self):
        print('{} {}'.format(self.__first_name, self.__last_name))

j = Person('Martin', 'Luther King')
j.print_full_name

