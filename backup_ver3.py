#!/usr/bin/env python
# encoding: utf-8

import time
import os

# source
source = ['/home/jack/test1']
# target_dir
target_dir = '/home/jack'
# today
today = target_dir + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(today):
    os.mkdir(today)
    print('Success make dirctory {}'.format(today))
# now
now = time.strftime('%H%M%S')
# target_name
target_name = today + os.sep + now + '.zip'
# zip_command
zip_command = 'zip -qr {} {}'.format(target_name, ''.join(source))

print(zip_command)
if os.system(zip_command) == 0:
    print('Sucess make backup file {}'.format(target_name))
else:
    print('Failed')
