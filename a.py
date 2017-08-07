#!/usr/bin/env python
# encoding: utf-8

<<<<<<< HEAD

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    # 间接调用
    def detail(self):
        print(self.name)
        print(self.age)


# 直接调用
#obj1 = Foo('Tom', 18)
#print(obj1.name)
#print(obj1.age)
#
#obj2 = Foo('Jack', 20)
#print(obj2.name)
#print(obj2.age)

# 间接调用
obj1 = Foo('Tom', 18)
obj1.detail()
=======
class Foo(object):
    def __init__(self, name):
        self.name = name

    def Hello(self):
        print('hello,{}'.format(self.name))

obj = Foo('tom')
obj.Hello()
>>>>>>> dd270fb97fea2d5161417be680ef66022fbea70e
