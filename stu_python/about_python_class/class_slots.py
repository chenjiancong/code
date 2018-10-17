#!/usr/bin/env python
# encoding: utf-8
# __slots__ 限制属性,使类不能随意增加属性

class Student(object):
#    __slots__ = ('name', 'score') # 使用tuple 定义允许绑定的属性

    def __init__(self, name, score):
        self.name = name
        self.score = score

#    def set_name(self, name):
#        self.name = name
#
#    def set_score(self, score):
#        self.score = score


s = Student('aa',99)
print(s.name)
s.score = 90
print(s.score)
s.age = 14
print(s.age)
