#!/usr/bin/env python
# encoding: utf-8

import os
import time

# source
source = ['/home/jack/test1']
# target_dir
target_dir = '/home/jack'
# make directory
today = target_dir + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(today):
    os.mkdir(today)
    print('Make directory: {}'.format(today))
now = time.strftime('%H%M%S')
# target_name
target_name = today + os.sep + now + '.zip'
# zip_command
zip_command = 'zip -qr {} {}'.format(target_name, ''.join(source))

print(zip_command)
if os.system(zip_command) == 0:
    print('Success backup {}'.format(target_name))
else:
    print('Failed')


