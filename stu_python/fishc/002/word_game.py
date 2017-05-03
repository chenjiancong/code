#!/usr/bin/env python
# encoding: utf-8

temp = input("输入猜测的数值： ")
guess = int(temp)

if guess == 4:
    print("你猜对了！")

else:
    print("猜错了")
    print("数值是 4 ")

print("游戏结束")
