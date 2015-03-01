#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: regex.py

import re

pattern = re.compile(r'\d*')
match = pattern.search('13690891044')

print match.group()


pattern1 = re.compile(r'\w*-\d{3}')
#print pattern1.findall('hello-123 abc-1 dfadf-111')
match2 = 'hello-123 abc-1 dfadf-111'
print pattern1.findall('match2')
