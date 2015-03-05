#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: web_spider.py

import re
import urllib2
import urllib

#urllib
def getHtml(url):
    page_open = urllib.urlopen(url)
    page_read = page_open.read()
    return page_read

#print getHtml('http://www.baidu.com/')

#def getHtml(url):
#    request = urllib2.Request(url)
#    response = urllib2.urlopen(request)
#    page = response.read()
#    return page

#print getHtml('http://www.baidu.com/')

def getImg(html):
    regex = r"""pic_ext="jpeg".*? src="(.*?\.jpg)".*?"""
    patten = re.compile(regex)
    imglist = re.findall(patten,html)
    return imglist

html = getHtml('http://tieba.baidu.com/p/3614866491')
print getHtml(html)
