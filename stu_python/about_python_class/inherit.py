#!/usr/bin/env python
# encoding: utf-8
# About 类的多态
class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialize SchoolMember:{})'.format(self.name))

    def tell(self):
        # end = '' 使print显示不换行
        print('Name:{} Age:{}'.format(self.name, self.age), end = ' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{}'.format(self.salary))

t = Teacher('Jack',22, 3000)
#a = SchoolMember('aa', 11)
members = [t]
for i in members:
    i.tell()
