#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: class_student.py

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
#        self.grade = grade

    def print_score(self):
        print '%s:%d'%(self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            print 'A'
        elif self.score <90 and self.score >= 60:
            print 'B'
        else:
            print 'C'

Student('Tom',90).print_score()
Student('Jack',90).get_grade()

