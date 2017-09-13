#!/usr/bin/env python
# encoding: utf-8

L = []
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if x != y and y != z and x != z:
                L.append(x * 100 + y *10 + z)

print(L)
