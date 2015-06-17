#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: response_info.py

import urllib2

url = 'http://www.baidu.com'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.info()
