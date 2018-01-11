#!/usr/bin/env python
# encoding: utf-8


# 集合[1,1,1,2,2,2,3,3,4,4,5,6,7,7,8]，统计集合重复个数

lst = [1,1,1,2,2,2,3,3,4,4,5,6,7,7,8]

def statistics3(lst):
    m = set(lst)
    dic = {}
    for x in m:
        dic[x] = lst.count(x)
    return dic
print(statistics3(lst))

# 另一种方法
a = {i : lst.count(i) for i in set(lst)}
print(a)

for key,item in a.items():
    print('{}:{}'.format(key, item))
