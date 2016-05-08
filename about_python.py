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

#  print r'' 表示内部字符串默认不转义
print '\\\t\\'
print r'\\\t\\'

#大小写转换
s.upper()        #小写字母转换成大写字母
s.lower()        #大写字母转换成小写字母
s.capitalize()   #首字母转换成大写，其余小写
s.title()        #每个单词首字母大写，其余小写

#  迭代 d
d = {'Tom':90,'Merry':79,'Jack':89}
for values in d.itervalues():
    print values

for name, values in d.iteritems():
    print name, values

#  list迭代
for i, values in enumerate(['A', 'B', 'C']):
    print i, values

#  map, reduce 区别
map(f(x), range(10))
reduce(f(x, y), range(10))
map里的函数只接收1个参数, reduce函数里必须接收2个参数

#  Decorator 装饰器的功能就是将被装饰的函数当作参数传递给
#  装饰器对应的函数(名称相同的函数)，并返回包装后的被装饰的函数
例如打印名称
def name():
    print 'jack'

打印名称前打印uid
def uid(func):
    def wrapper(*arg, **kw):
        print 222
        return func(*arg, **kw)
    return wrapper

最终
@uid
def name():
    print 'jack'

#  222
#  jack
