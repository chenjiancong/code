#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: web_spider.py

import re
import urllib2
import urllib

#------------GetImg------------

#urllib 反应速度较快
def getHtml(url):
    page_open = urllib.urlopen(url)
    page_read = page_open.read()
    return page_read

#print getHtml('http://tieba.baidu.com/p/3614406057')

#urllib2 模拟浏览器,速度较慢,部分网站限制spider，如baidu.com
#def getHtml(url):
#    request = urllib2.Request(url)
#    response = urllib2.urlopen(request)
#    page_read = response.read()
#    return page_read
#
#print getHtml('http://tieba.baidu.com/p/3614406057')

def getImg(html):
    regex = r'src="(http://imgsrc.*?\.jpg)"'
    patten = re.compile(regex)
    imglist = re.findall(patten,html)
    return imglist

html = getHtml('http://tieba.baidu.com/p/3614406057')
print getImg(html)
print len(getImg(html))
