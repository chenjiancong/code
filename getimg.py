#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: getimg.py

import re
import urllib

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#print gethtml('http://bohaishibei.com/post/7883/')

def getimg(html):
    regex = r'<img.*? src="(.+?.jpg)"title.+?>'
    patten = re.compile(regex)
    url = re.findall(patten,html)
    return url

html = gethtml('http://bohaishibei.com/post/7883/')
print getimg(html)
