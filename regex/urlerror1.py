#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: urlerror1.py

import urllib2

#request = urllib2.Request('http://www.verycd.com/1')
#try:
#    urllib2.urlopen(request)
#except urllib2.URLError,e:
#    print e.reason

#403
#req = urllib2.Request('http://bbs.csdn.net/callmewhy')

req = urllib2.Request('')
try:
    urllib2.urlopen(req)
except urllib2.URLError,e:
    print e.code
