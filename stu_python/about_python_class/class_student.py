#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('Score:{}'.format(self.score))

    def get_grade(self):
        if self.score >= 90:
            print('A')
        elif 80 <= self.score < 90:
            print('B')
        else:
            print('C')

t = Student('tom', 81)
t.print_score()
t.get_grade()
