#Filename: about_python.txt
#-*- coding:utf-8 -*-
# Somethig about python

# Time
# From: http://www.cnblogs.com/wanpython/archive/2010/08/07/1794598.html
time.strftime('%Y-%m-%d',time.localtime(time.time()))
example: 2010-07-19

time.strftime里面有很多参数，可以让你能够更随意的输出自己想要的东西：
下面是time.strftime的参数：
strftime(format[, tuple]) -> string
将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出

python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

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

# set 重复元素自动过滤重复值
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


# 2017.08.10 函数式编程
# lambda 匿名函数
add = lambda a, b: a + b
print(add(2, 3))

# map 映射
map(func, *iterables)
map(len, ['a', 'aa'])

# reduce 迭代
from functools import reduce # 使用前要导入
reduce(lambda a, b: a + b, [1, 2])

#  map, reduce 区别
map(f(x), range(10))
reduce(f(x, y), range(10))
map里的函数只接收1个参数, reduce函数里必须接收2个参数

# filter 过滤
filter(func or None, iterator)

# sorted 排序
sorted(iterator, func or None) # 默认升序排列, 降序 reverse = True
sorted([-1,1,-2], key=abs)

# sort 与 sorted 区别: sort是在原位重新排列列表,sorted()是产生一个新列表
l = [1,0,-1,2]
l.sort()
sroted(l)

# 关于大小写转换
s.upper()        #小写字母转换成大写字母
s.lower()        #大写字母转换成小写字母
s.capitalize()   #首字母转换成大写，其余小写
s.title()        #每个单词首字母大写，其余小写

# find() index()
info = 'abcd'
print(info.find('a')) # 如果有就返回 0, 没有返回 -1
print(info.index('a')) # 如果有就返回 0, 没有返回报错

# Iteration 迭代 给定一个list 或 tuple， 可以通过for 循环来遍历这个list 或 tuple
# Decorator 装饰器的功能就是将被装饰的函数当作参数传递给
# 装饰器对应的函数(名称相同的函数)，并返回包装后的被装饰的函数
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
class Foo(object):

    # 创建类中的函数
    def Bar(self):
        print('Bar')

    def Hello(self, name):
        print('i am %s' %name)

# 根据类Foo创建对象obj
obj = Foo()
obj.Bar()
obj.Hello('Jack')

# 封装
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

obj1 = Foo('Tom', 18)
obj2 = Foo('Jack', 20)

# 2017.08.09
# 继承
class Animal(object):
    pass

class Dog(Animal):
    pass

# 多态
class Animal(object):
    def run_twice(animal):
        animal.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

# 2017.08.05
# format格式化字符串
1,不需要理会数据类型
2,填充方式灵活
print('hello {0}'.format('world'))
print('hello {}, i am {}.nice to meet {}'.format('tom', 'jack', 'tom'))
print('hello {name1}'.format(name1='jack'))


