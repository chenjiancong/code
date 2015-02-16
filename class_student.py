#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: class_student.py

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s:%d'%(self.name,self.score)

Student('Tom','90').print_score()

