#!/usr/bin/env python
# encoding: utf-8

# write
with open('/home/jack/test1/readme.txt', 'a+') as f:
    f.write('Hello4')
    f.write('Hello5')

# read
with open('/home/jack/test1/readme.txt', 'r') as f:
	print(f.read())
