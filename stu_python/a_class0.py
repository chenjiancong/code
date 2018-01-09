#!/usr/bin/env python
# encoding: utf-8

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        return 'A'

p1 = Person('Bob', 43)
print(p1.get_grade())
