#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: about_python_字符编码.py

python 中 ASCII 码相互转换
>>> ord('A')
65

>>> chr(65)
'A'

表示 Unicode 字符串 u'...'
u'中'
>>>u'\u4e2d'

Unicode 转换成 utf-8 用 .endcode('utf-8')
>>>u'中'.encode('utf-8')
'\xe4\xb8\xad'

把 utf-8 转换成 Unicode 用.decode('utf-8')
print '\xe4\xb8\xad'.decode('utf-8')


