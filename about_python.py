#Filename: about_python.txt
#-*- coding:utf-8 -*-
#Somethig about python

#赋值
'='                   #赋值，先计算右侧的表达式
EX
a = 'ABC'
b = a
a = 'XYZ'
print b
输出是 ‘ABC’

#字符编码
ASCII里，A = 65,z = 122
>>>ord('A')
65
>>>chr(65)
A
>>>print u'中文'
中文
>>>u'中'
u'\u432d'

#格式化字符串
print 'hello,%s'%('jack')
print 'hello,{name}'.format(name='jack')