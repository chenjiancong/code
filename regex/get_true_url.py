#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: get_true_url.py

import urllib2

short_url = 'http://rrurl.cn/b1UZuP'
request = urllib2.Request(short_url)
response = urllib2.urlopen(request)
true_url = web_response.geturl()

print true_url
