#!/usr/bin/env python
# encoding: utf-8

import os
import time

# source
source = '/home/jack/test1'
# backup_dir
target_dir = '/home/jack'
# name
target_name = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# command
zip_command = 'zip -qr {} {}'.format(target_name, source)

print(zip_command)
if os.system(zip_command) == 0:
    print('Success backup {}'.format(target_name))
else:
    print('Failed')
