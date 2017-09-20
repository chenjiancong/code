#!/usr/bin/env python
# encoding: utf-8

from sys import argv

script, from_file, to_file = argv

print('From file is:{}'.format(from_file))
print('To file is:{}'.format(to_file))
print('Truncate the {}'.format(to_file))

#with open(from_file, 'r') as f:
#    f.read()
data = open(from_file, 'r')
indata = data.read()
data.close()

target = open(from_file, 'r')

with open(to_file, 'a') as f:
    f.write(indata)
