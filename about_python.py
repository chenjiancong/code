#Filename: about_python.txt
#-*- coding:utf-8 -*-
#Somethig about python

#显示内置函数(BIF) Build-in funcations
>>>dir(__builtins__)

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

# list,tuple,dict,set
# list 1,元素可变;2,查找和插入时间随元素增加而增加；3,占内存小
classmates = ['Tom', 'Jack', 'Marry']
# 末尾追加元素
classmates.append('Adam')
# 插入到指定位置
classmates.insert(1,'Peter')
# 删除指定元素 i为索引位置
classmates.pop(i)

# tuple
t = ('a', 'b', 'c')

# dic 1,查找和插入速度快，不随key增加而变慢；2,需求占用大量内存;3,dict的key必须是不可变
name = {'Tom':98, 'Jack':89, 'Marry':79}
# 显示Jack成绩
name['Jack']

# 修改成绩
name['Tom'] = 77

# 删除 pop(key)
name.pop('Marry')

# set 重复元素自动过滤
s = set([1, 1, 2, 3, 3])
>>s
{1,2,3}

#  迭代 d
d = {'Tom':90,'Merry':79,'Jack':89}
for values in d.itervalues():
    print values

for name, values in d.iteritems():
    print name, values

#  list迭代
for i, values in enumerate(['A', 'B', 'C']):
    print i, values

# 函数参数
# 默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#  map, reduce 区别
map(f(x), range(10))
reduce(f(x, y), range(10))
map里的函数只接收1个参数, reduce函数里必须接收2个参数

# Iteration 迭代 给定一个list 或 tuple， 可以通过for 循环来遍历这个list 或 tuple


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

算法：
a + b + c + ...
sum = 0
for i in numbers:
#    sum = sum + i
    sum += i
return sum

# 2017.08.04
'''
# 面向对象编程 Object Oriented Programming
面向过程:根据业务逻辑从上向下写代码
函数式:将功能代码封装到函数中,日后开发无需重复编写(
函数式的应用场景 -> 各个函数之间是独立且无共用的数据
)
面向对象:对函数进行分类和封装.  类和对象的使用

1,class 类就是一个模板,模板里包含多个函数,函数实现一些功能;
2,对象则是根据模板创建的实例,通过实例对象执行类中的函数
3,类中的函数,第一个参数必须是 self;类中定义的函数叫 '方法'
4,面向对象三大特性: 封装 继承 多态
'''
# 创建类
class Foo:

    # 创建类中的函数
    def Bar(self):
        print('Bar')

    def Hello(self, name):
        print('i am %s' %name)

# 根据类Foo创建对象obj
obj = Foo()
obj.Bar()
obj.Hello('Jack')

