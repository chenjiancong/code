#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: get_img.py

import re
import urllib

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#print get_html("http://tieba.baidu.com/p/3553794829")

def get_img(html):
    reg = 'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

html = get_html("http://tieba.baidu.com/p/3553794829")
print get_img(html)

