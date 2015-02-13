#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename: str.py

#ord('字母'),将字母转换成ASCII码
str = raw_input('输入一个要查ASCII的字母:')
print '%s ==>> ASCII is: '%str,ord(str)

#chr(数值),将数值转换成对应的字母
str2 = int(raw_input('输入一个要转换成字母值:'))
print '%d ==>> 对应字母:'%str2,chr(str2)
