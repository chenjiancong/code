#!/usr/bin/env python
# encoding: utf-8

def fun1():
    print("fun1...")
    def fun2():
        print("fun2...")
    fun2()

fun1()

def funx(x):
    def funy(y):
        return x * y
    return funy()


def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()

fun1()
