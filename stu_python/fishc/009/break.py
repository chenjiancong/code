#!/usr/bin/env python
# encoding: utf-8

bingo = '说中了'
guess = input("输入些文字： ")

while True:
    if guess == bingo:
        break
    guess = input("错了，再输入：")
print("游戏结束")

