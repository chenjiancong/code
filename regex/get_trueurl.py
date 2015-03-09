#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: geturl.py

import urllib2

old_url = 'http://rrurl.cn/b1UZuP'
request = urllib2.Request(old_url)
response = urllib2.urlopen(request)
print 'Real url:',response.geturl()

