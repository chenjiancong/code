#!/usr/bin/env python
# encoding: utf-8

import random
secret = random.randint(1, 10)
running = True
times = 3

while running and times > 0:
    guess = int(input("输入猜测的数： "))
    times = times - 1
    if guess == secret:
        print("你猜对了")
        break
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
print("游戏结束")
