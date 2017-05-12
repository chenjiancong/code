#!/usr/bin/env python
# encoding: utf-8

def MyFirstFunction(name):
    '这个是函数文档，当使用 MyFirstFunction.__doc__ ,将会被调用出来'
    #这个是注释，调用函数文档不会被显示出来
    print("Hello, " + name)

MyFirstFunction('jack')
MyFirstFunction.__doc__

def SecondFunction(name, word):
    print(name, '-->', word)

SecondFunction('Tom', 'Fuck U')

def ThirdFunction(name = 'Peter', word = 'Nothing'):
    print(name, 'say: ', word)

ThirdFunction(name = 'jdfk',word ='Hello World')

def LotFunction(*funct):
    print(len(funct))
    print(type(funct))

LotFunction('adkfjdsaf, 123, {akdsfjdasf}', 123123)
