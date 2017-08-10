#!/usr/bin/env python
# encoding: utf-8
# __slots__ 限制实例属性

class Student(object):
    __slots__ = ('name', 'gender') # 用tuple定义允许绑定的属性名称
    def __init__(self, name, gender, score):
        self.name = name
        self.gender  = gender
        self.score = score

    def set_score(self, score):
        self.score = score

a = Student('tom','F', 90)
#a.set_score(99)
print(a.score)
