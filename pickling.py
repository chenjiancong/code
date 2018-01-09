#!/usr/bin/env python
# encoding: utf-8

import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile,'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

# Read back from to storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)

