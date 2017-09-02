#!/usr/bin/env python
# encoding: utf-8

# 导入使用的模块
import os
import time

# 需要备份的目录
source = ['/home/jack/test1/test.txt']
# 备份放置路径
target_dir = '/home/jack'
# 备份的命名
target_name = 'aa' + '.zip'
#target_name = target_dir + os.sep + time.strftime('%Y%M%D%H%M%S') + '.zip'
# 备份命令
zip_command = "zip -r {} {}".format(target_name, target_dir)

print(zip_command)
if os.system(zip_command) == 0:
    print('Success backup {}'.format(target_name))
else:
    print('Failed')
