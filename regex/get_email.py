#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: get_email.py

import re
import urllib
import urllib2

#use urllib
def getHtml(url):
    open_page = urllib.urlopen(url)
    page_read = open_page.read()
    return page_read

#use urllib2
def getHtml(url):
    request = urllib2.Request(url)
    respont = urllib2.urlopen(request,timeout=10)
    page_read = respont.read()
    return page_read

#print getHtml('http://wenq.org/wqy2/index.cgi?FAQ')

def getEmail(html):
    regex = r'admin.+? *\.org'
    pattern = re.compile(regex)
    email = re.findall(pattern,html)
    return email

html = getHtml('http://wenq.org/wqy2/index.cgi?FAQ')
print getEmail(html)





