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
    regex = r'pic_ext="jpeg".+? src="(.+?\.jpg)".+?'
    patten = re.compile(regex)
    url = re.findall(patten,html)
    return url
   # x = 0
   # for img in url:
   #     urllib.urlretrieve(img,"%s.jpg"%x)
   #     x =x+1

html = gethtml('http://tieba.baidu.com/p/3614866491')
print getimg(html)
print len(getimg(html))
