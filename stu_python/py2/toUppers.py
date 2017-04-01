#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: toUppers.py

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print toUppers(['hello','Aa',111,'TTT'])

