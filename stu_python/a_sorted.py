#!/usr/bin/env python
# encoding: utf-8

# about sorted

# 要求1.正数在前负数在后 2.正数从小到大 3.负数从大到小
list1 = [7, -8, 5, 4, 0, -2, -5]

a = sorted(list1, key=lambda x:(x<0, abs(x)))
print(a)

# 按年龄排序
students = [('john', 15), ('jane', 12), ('dave', 10)]
b = sorted(students, key=lambda x:x[1])
print(b)

