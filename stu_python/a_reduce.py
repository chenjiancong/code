#!/usr/bin/env python
# encoding: utf-8


# 集合[1,1,1,2,2,2,3,3,4,4,5,6,7,7,8]，统计集合重复个数
# reduce 使用要先导入
# from functools import reduce
# 每一次迭代，都将上一次的迭代结果

def statistics2(lst):
    m = set(lst)
    dic = {}
    for x in m:
        dic[x] = lst.count(x)
    return dic
lst = [1,1,1,2,2,2,3,3,4,4,5,6,7,7,8]
print(statistics2(lst))

def statistics3(lst):
    m = set(lst)
    dic = {}
    for x in m:
        print(x)
lst = [1,1,1,2,2,2,3,3,4,4,5,6,7,7,8]
print(statistics3(lst))

