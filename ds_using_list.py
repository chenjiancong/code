#!/usr/bin/env python
# encoding: utf-8

shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for items in shoplist:
    print(items, end= '')
