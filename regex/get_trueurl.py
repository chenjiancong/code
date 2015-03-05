#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: geturl.py

from urllib2 import Request,urlopen,URLError,HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
request = Request(old_url)
response = urlopen(request)
print 'Real url:',response.geturl()

