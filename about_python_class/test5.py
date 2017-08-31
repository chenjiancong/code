#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    def __init__(self, name, score):
        self.name   = name
        self.score  = score

    def Get_name(self, name):
        print(self.name)

t = Student('tom', 90)
print(t.Get_name())
