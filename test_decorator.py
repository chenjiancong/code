#!/usr/bin/env python
# encoding: utf-8

def func1(n1):
    def func2(n2):
        print(n2)
        return n1 + n2
    return func2

a = func1(20)
print(a(100))

def func2(func):
    def worker(*args, **kw):
        print('call {}'.format(func.__name__))
        return func(*args, **kw)
    return worker
@func2
def Hello():
    print('Hello')

a = Hello
print(a())

d={'tom':90, 'peter':80}
for i in d.values():
    print(i)

for k, v in d.items():
    print(k, v)
