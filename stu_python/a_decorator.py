#!/usr/bin/env python
# encoding: utf-8

from functools import reduce
import time

def print_runtime(func):
    def func1(*args, **kw):
        t1 = time.time()
        r = func(*args, **kw)
        t2 = time.time()
        t3 = time.strftime('%Y-%m-%d %H:%M:%S')
        print('Func is:{},run_time:{}'.format(func.__name__, (t2 - t1)))
        print('Print time:', t3)
        return func(*args, **kw)
    return func1

@print_runtime
def func0(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(func0(10))
