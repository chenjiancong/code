#!/usr/bin/env python
# encoding: utf-8

# 查找一个集合里最大或者最小的N个元素列表
# heapq 模块有两个函数: nlargest(), nsmallest() 可以处理

import heapq

nums = [1, 6, 4, 23, -4, 0, 4, 53]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 另一种方法

smallest = sorted(nums)
largest = sorted(nums, reverse = True)
print(smallest[0:3])
print(largest[0:3])

# 接收一个key，用于更复杂的数据结构
portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
cheap = heapq.nsmallest(3, portfolio, key = lambda s:s['price'])
expensive = heapq.nlargest(3, portfolio, key = lambda s:s['price'])
print(cheap)
print(expensive)
