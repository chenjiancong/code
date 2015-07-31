#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: first_upper.py

def first_upper(s):
    return s[0].upper() + s[1:].lower()

print map(first_upper,['tom','MERRY','JaCk'])

