#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: getimg.py

import re
import urllib

def get_url(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#print get_url('http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html')

def get_img(html):
    regex = r'src="(.+?\.png)"'
    patten = re.compile(regex)
    img_url = re.findall(patten,html)
#    return img_url
    x = 1
    for img in img_url:
        urllib.urlretrieve(img,'%s.jpg'%x)
        x +=1

html = get_url('http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html')
get_img(html)







