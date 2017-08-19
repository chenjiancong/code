#!/usr/bin/env python
# encoding: utf-8

# 可变参数
def func1(*numbers):
    sum = 0
    for i in numbers:
#        sum = sum + i
        sum += i
    return sum

s = func1(1,3,4)
print(s)

# 关键字参数
def person(name, age, **kw):
    print('name:',name,
            'age:',age,
            'other',kw)

p = person('Tom',30,city='BJ')

# 限制关键字参数的名字
def person1(name, age, *, city, job):
    print('name:',name,
            'age:',age,
            'city:',city,
            'job:',job)

p1 =person1('aa',20,city='bj',job='worker')

# 关键字参数可以有默认参数
def person2(name, age, *, city='GZ', job):
    print('name:',name,
            'age:',age,
            'city:',city,
            'job:',job)

p2 =person2('bb',20,job='worker')

