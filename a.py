#!/usr/bin/env python
# encoding: utf-8


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
