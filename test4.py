#!/usr/bin/env python
# encoding: utf-8

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creates = jars / 100
    return jelly_beans, jars, creates

start_point = 1000
beans, jars, creates = secret_formula(start_point)

print('With a starting point of: {}'.format(start_point))
print('We\'d have {} beans, {} jars, and {} creates.'.format(beans, jars, creates))

start_point = start_point / 10
