#Filename: about_python.txt
#-*- coding:utf-8 -*-
# Somethig about python

# Some Tips

#URI Uniform Resource Identifier 统一资源标识符
#URL Uniform Resource Locator 统一资源定位符

# 2017.09.20
# def (define) 定义

# 2017.09.01
# python中有三种数：整数、浮点数、复数
# 浮点数 3.23 、 5E-1 （即5 *10）
# 复数(-5+4j)
# aa=123-12j
# print(aa.real)
# print(aa.imag)

# 无效的标识符： 2things, this is, my-name

# str.replace() 替换函数
str.replace(rgExp, replaceText, max)
s1.replace('a', 'b', 3) # 将a 替换成 b 最多3次

# break, continute
# break
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    print('Length is ',len(s))
print('Done')

# continue


# About 赋值
'='                   #赋值，先计算右侧的表达式
EX
a = 'ABC'
b = a
a = 'XYZ'
print b
输出是 ‘ABC’

# 字符编码
ASCII里，A = 65,z = 122
>>>ord('A')
65
>>>chr(65)
A
>>>print u'中文'
中文
>>>u'中'
u'\u432d'

# 我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'


#显示内置函数(BIF) Build-in funcations
>>>dir(__builtins__)

# 2017.08.11 About 函数带括号与不带括号的区别
#带括号指的是返回结果
#不带括号是执行函数

# 2017.08.14 查询类型
type('a')
isinstance('a', str)

# 2017.08.24 对象的三个要素:id, type, value
# id用来唯一标识一个对象;type标识对象的类型;value是对象的值

# About Time
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

# 2017.08.05 About format格式化字符串
1,不需要理会数据类型
2,填充方式灵活
print('hello {0}'.format('world'))
print('hello {}, i am {}.nice to meet {}'.format('tom', 'jack', 'tom'))
print('hello {name1}'.format(name1='jack'))

# About list,tuple,dict,set
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

# dic 1,查找和插入速度快，不随key增加而变慢；2,需要占用大量内存;3,dict的key必须是不可变
name = {'Tom':98, 'Jack':89, 'Marry':79}
# 显示Jack成绩
name['Jack']

# 修改成绩
name['Tom'] = 77

# 删除 pop(key)
name.pop('Marry')

# 字典的遍历
d = {'Tom':80, 'Jack':66}
# key, values的遍历
for key, value in d.items()
    print(key, value)

# 仅values的遍历
for value in d.values():
    print(value)

# set 重复元素自动过滤重复值
s = set([1, 1, 2, 3, 3])
>>s
{1,2,3}

#  list遍历, enumerate,将下标循环出来
for i, values in enumerate(['A', 'B', 'C']):
    print i, values
0 A
1 B
2 C

# About 切片 2017.09.02
# shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist[:] # 返回整个列表
shoplist[1:3] # 返回1开始，包括位置2
shoplist[:-1] # 返回除最后一个的切片
shoplist[::3] # 第三个参数是切片步长
shoplist[::-1]  # 反向取整个列表

# 2017.08.20 迭代与遍历的区别
# 迭代时数据可以是未生成的；
# 遍历时数据已经钦定

# Generator 生成器
# 列表元素按算法推导，一边循环一边计算，称为生成器: generator
# 只需求将列表生成式(List Comprehensions)的[]改为()，就创建了 generator
# 列表生成式 L = [x * x for x in range(10)]
 generator  g = (x * x for x in range(10))
# 调用的算法可以是next(g),或者用for
for n in g:
    print(n)
# yield 如果一个函数(def)里包含yield，那这个函数就是一个generator

# 2017.08.23
# 迭代器
# 可迭代对象定义：
# 集合数据，如list,tuple,dict,set,str等；生成器generator,generator funceiton
# 这些可以直接作用for循环的对象统称为可迭代对象： Iterable
 判断一个对象能否迭代
isinstance('abc', Iterable) >>> True
isinstance(123, Iterable) >>> False

# About 函数参数
# 参数的顺序：必选参数、默认参数、可变参数、关键字参数
# 默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 调用的时候要这样: add_end([1, 2])
# 2017.08.21 另一种写法
def func1(*args):
    L = list(args)
    if L == None:
        L = []
    L.append('End')

# is 与 == 的区别
# is拿id作为判断因素； == 拿 value 作为判断因素

   return L

# 2017.08.19 About *args **kw
# *args 即 asterisk args
# *args, 可变参数,可以传入任意个参数，包括0个参数
# *args 参数args 接收到的是tuple
def func1(*args):
    for i in args:
        print(i)

# **kw，关键字参数,允许传入0或任意个参数，参数将自动组装成dict
def person(name, age, **kw):
    print(name, age, kw)
p = person('tom', 10, city=BJ)
# 限制关键字参数的名字
# 1,使用 * 分隔；2,如果前面有可变参数*args,可以不用*;3,可以添加默认参数
def person1(name, age, *, city):
    print(name, age, city)
p1 = persion1('aa', 10, city='BJ')

def person22(name, age, *, city='GZ'):
    print(name, age, city)
p2 = persion2('aa', 10)

# 2017.08.10 函数式编程
# lambda 匿名函数
add = lambda a, b: a + b
print(add(2, 3))

# map 映射
map(func, *iterables)
map(len, ['a', 'aa'])

# reduce 迭代
# reduce 把结果继续和序列的下一个元素做累积计算

from functools import reduce # 使用前要导入
reduce(lambda a, b: a + b, [1, 2])

#  map, reduce 区别
map(f(x), range(10))
reduce(f(x, y), range(10))
# map里的函数只接收1个参数, reduce函数里必须接收2个参数

# map, reduce 在python3里的延迟计算,变成生成器，需要时才生成。所以用list或用for查看生成
# 可以简单把map,reduce的返回值看成是一个集合
# map,reduce --> list

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
# eg 'This is test'
s.title()        #每个单词首字母大写，其余小写
# eg 'This Is Test'

# find() index()
info = 'abcd'
print(info.find('a')) # 如果有就返回 0, 没有返回 -1
print(info.index('a')) # 如果有就返回 0, 没有返回报错

# Iteration 迭代 给定一个list 或 tuple， 可以通过for 循环来遍历这个list 或 tuple

# About Decorator
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

# 求和、求阶乘的方法
# 求和1
def fun1(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum

# 求和2
def fun2(n):
    sum, i = 0, 1
    while n - i >= 0:
        sum = sum + i
        i   = i + 1
    return sum

# 阶乘1
from functools import reduce
def func1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1)) # 由1开始，不然结果为0

def func2(n):
    if n == 1:
        return 1
    return n * func2(n - 1)

# 2017.08.24 About Partial function 偏函数
# 就是自定义一个函数，并绑定默认值
# 使用前要导入 import functools
import functools
int2 = functools.partial(int, base=2)
int('1000')
# 相当于  int('1000', base=2)

# 2017.08.04 About OOP 面向对象编程
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
4,类的特性: 封装 继承 多态
5,类的成员: 字段 方法 属性
'''

'''
类的风格：
class 应该使用 'camel case 驼峰式大小写'，例如 SuperGoldFactory 而不是super_gold_factory
其他函数应该使用 'underscore format 下划线隔词'，例如 my_awesome_hair 而不是 myawesomehair
'''
# 命名约定: 1,大写方法名称的首字母;2,使用一个唯一的小字符串作为数据属性名称前缀

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

# 2017.08.29 About 限制访问 private
"""
也就是实例化之后不允许访问；
假如另外再次定义还是可以访问
"""
class Student(object):
    def __init__(self, name, score):
    # 设置为private
        self.__name = name
        self.__score = score

    # 设置访问
    def get_name(self):
        return self.__name = name

    # 设置修改
    def set_score(self, score):
        self.__score = scre

tom = Student('Tom', 80)
'''
当外部要访问时
tom.get_name()

当外部要修改时
tom.set_score = 99
'''
# About __slots__ 限制实例属性;优化内存(但不利于代码维护)
# 仅对当前类实例起作用,对继承的子类不起作用

'''
python 能动态增加类增加类
比如
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student('tom', 99)
然后可以增加类
s.age = 15
但如果使用了 __slots__ 限定了类就不能增加
'''
class Student(object):
    __slots__ = ('name', 'age') # 用tuple 定义允许绑定的属性名称(允许修改的属性)

# private 与 __slots__ 区别。前者是限制属性的访问，后者是控制属性的增加

# 2017.08.09 About 继承、多态
# 继承

class Animal(object):
    pass

class Dog(Animal):
    pass

# 多态
class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print('Name:{}, Age:{}'.format(self.name, self.age), end = ' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        print('Salary:{}'.format(self.salary = salary))

t = Teacher('Jack', 18, 3000)
member = [t]
for i in member:
    i.tell()

# @property 将方法变成属性,限制访问


# About I/O 读取
# with ... as ... 自动调用close()
# read 读
>> with open('path', 'r') as f
    print(f.read())

# read 写
>> with open('path', 'w') as f:
    f.write('hello world')

# read() 一次读取全部内容;
# read(size) 每次最多读取size个字节
# readline() 每次读取一行内容
# readlines() 一次读取所有内容并按行返回list
# truncate()

# 2017.09.16 操作属性
r 只读模式(read)
r+ 读写模式指针放在开头
w 写入。如果存在则覆盖，不存在就创建(write)
w+ 读写模式。如果存在则覆盖，不存在就创建
a 打开一个文件追加。如果存在，指针放在结尾。如果不存在就创建(append)
a+ 读写模式。如果存在，指针放在结尾。如果不存在就创建

# 2017.09.08 操作目录
import os
# os.mkdir 创建目录
'''
创建目录时，不要直接拼字符串，而要通过os.path.join()
这样是为了处理不同系统的路径分隔符。如linux: home/jack; win: d:\abc
拆分路径时使用os.path.split()
'''
os.path.join('/home/jack/test1', 'abc')
# os.path.split('/home/jack/test.txt') >>> ('/home/jack', 'test.txt')

os.mkdir('/home/jack/test1/abc')
# os.rmdir 删除目录
os.rmdir('/home/jack/test1/abc')

# os.rename() 重命名
os.rename('test.txt', 'test.py')
# os.remove() 删除文件
os.remove('test.py')
