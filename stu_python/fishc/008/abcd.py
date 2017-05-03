#!/usr/bin/env python
# encoding: utf-8

number = int(input("输入一个分数: "))

if number >= 90:
    print("分数为：A")
#else:
#    if 90 > number >= 80:
#        print("分数为:B")
#    else:
#        if 80 >number >= 70:
#            print("分数为:C")
#        else:
#            print("分数为:D")

elif 90 > number >= 80:
    print("分数为：B")
elif 80 > number >= 70:
    print("分数为：C")
else:
    print("分数为:D")

