#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#Filename: python_time.py

import time

strftime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print strftime

