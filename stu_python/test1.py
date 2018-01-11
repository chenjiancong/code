#!/usr/bin/env python
# encoding: utf-8

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{name}:{score}'.format(name = self.name, score = self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            print('C')

bart = Student('Bart', 59)
bart.print_score()
bart.get_grade()
#print(bart.get_grade())
