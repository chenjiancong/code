#!/usr/bin/env python
# encoding: utf-8

import time, datetime;
localtime = time.localtime(time.time())
print('Local current time:', localtime)

expire_time = '2018-01-03 10:00:00'
d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
print(d)

d2 = time.strftime('%Y-%m-%d %H:%M:%S')
print(d2)
