#!/usr/bin/env python
# encoding: utf-8

score = ['aa', '88', 'bb', '77', 'cc', '66', 'dd', '55']
length = len(score)

#for i in range(length):
#    if i % 2 == 0:
#        print(score[i], '-->', score[i+1] )

i = 0
while i < length:
    print(score[i], '->', score[i+1])
    i += 2
