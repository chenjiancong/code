#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: class_init.py

"类名首字母通常大写,没有继承可写object"
class Persion(object):
    "初始化self,name,__init__第一个参数永远是self"
    def __init__(self,name):
        self.name = name
    def sayhi(self):
        print 'Hello,i\'m %s'%self.name

Persion('Jack').sayhi()
p = Persion('Tom')
p.sayhi()


