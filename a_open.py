#!/usr/bin/env python
# encoding: utf-8

from sys import argv

script, filename = argv

# 另一个方法
#txt = open(filename)
#print('Here\'s your file{}:'.format(filename))
#print(txt.read())

#print('Type the filename again:')
#file_again = input('> ')
#txt_again = open(file_again)
#print(txt_again.read())

# 简易方法
with open(filename, 'r') as f:
    #f.read()
    print(f.read())
