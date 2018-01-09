#!/usr/bin/env python
# encoding: utf-8

# 100 以内的奇数有哪些
L = [i * 1 for i in range(1, 101) if i %2 == 1]
print(L)

def fib(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a + b

for n in fib(15):
    print(n)

m = fib(13)
print(m)
m.next()
