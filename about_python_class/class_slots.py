#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    __slots__ = ('name') # 使用tuple 定义允许绑定的属性

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def set_name(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score


s = Student('aa',99)
print(s.name)
