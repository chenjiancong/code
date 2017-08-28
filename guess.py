#!/usr/bin/env python
# encoding: utf-8


#number = 10
#guess_number = int(input('Enter Your Guess:'))
# if
#if number == guess_number:
#    print('Right')
#elif guess_number > number:
#    print('Too Bigger')
#else:
#    print('Too Smaller')

# while
import random
secert = random.randint(1, 10)
Running = True
Times = 3

while Running and Times> 0:
    guess_number = int(input('Enter Number:'))
    Times = Times -1
    if guess_number > secert:
        print('Too Bigge')
    else:
        if guess_number < secert:
            print('Too Smaller')
        else:
            print('Right')
            break
