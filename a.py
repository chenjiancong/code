#!/usr/bin/env python
# encoding: utf-8

def adda(number):
    def addb(number_in):
        print('number_in:',number_in)
        return number + number_in
    return addb

v1=adda(1)
print(v1(100))
