#!/usr/bin/env python
# encoding: utf-8

# break

#while True:
#    s = input('Enter something:')
#    if s == 'quit':
#        break
#    else:
#        print('len(s) is: ', len(s))
#print('Done')

while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    elif len(s) < 3:
        continue
    else:
        print('len(s) is: ', len(s))
print('Done')
