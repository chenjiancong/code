#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: try_except.py

import urllib2

try:
    response = urllib2.urlopen('http://bbs.csdn.net/why')
except urllib2.HTTPError,e:
    print e.code


