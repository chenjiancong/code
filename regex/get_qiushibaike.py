#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: qiushibaike.py
#抓取糗事百科的文章

import re
import urllib
import urllib2

#use urllib
#def getHtml(url):
#    open_page = urllib.urlopen(url)
#    page_read = open_page.read()
#    return page_read
#
#print getHtml('http://www.qiushibaike.com/hot/page/1')

#use urllib2
#抓取网页代码
#部分网站屏蔽爬虫,需要添加headers验证
user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0'
headers = {'User-Agent' : user_agent}
def getHtml(url):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    page_read = response.read()
    return page_read

#要加‘http://’
#print getHtml('http://www.qiushibaike.com/hot/page/1')

#编写正则表达式
def getInfo(html):
    regex = r'class'
    pattern = re.compile(regex)
    info = re.findall(pattern,html)
    return info

html = getHtml('http://www.qiushibaike.com/hot/page/1')
print getInfo





