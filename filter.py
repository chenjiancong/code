#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: filter.py

#filter(函数,list) ==> list #将一组数放入函数中，若输出的函数为True则输出

print filter(lambda x:x%2 ==0,range(1,11))
