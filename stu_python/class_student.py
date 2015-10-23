#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: class_student.py

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
#        self.grade = grade

    def print_score(self):
        print '%s:%d'%(self.__name,self.__score)

    def get_grade(self):
        if self.__score >= 90:
            print 'A'
        elif self.__score <90 and self.__score >= 60:
            print 'B'
        else:
            print 'C'

#允许外部访问get_name,get_score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

#允许外部修改score
    def set_score(self,score):
        self.__score = score

Tom = Student('Tom',88)
Jack = Student('Jack',50)
Tom.print_score()
Tom.name = 'Tom Simpson'
#Jack.print_score()
#Jack.get_grade()
#Student('Tom',90).print_score()
#Student('Jack',90).get_grade()

