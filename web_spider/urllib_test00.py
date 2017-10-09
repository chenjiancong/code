#!/usr/bin/env python
# encoding: utf-8

import urllib.request
import requests

#response = urllib.request.urlopen('http://www.baidu.com')
#html = response.read()
#print(html)

url = 'http://www.baidu.com'

user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;)'

headers = {'User-Agent': user_agent}

req = urllib.request(url, headers = headers)

response = urllib.request.urlopen(req)

the_page = response.read()

print(the_page)
