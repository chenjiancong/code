#!/usr/bin/env python
# encoding: utf-8

# 导入使用的模块
import os
import time

# 需要备份的目录
source = '/home/jack/test1'
# 备份放置路径
target_dir = '/home/jack/back_up'
# 备份的命名
#target_name = 'bb' + '.zip'
target_name = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#target_name = target_dir + os.sep + 'aa' + '.zip'
# 备份命令
zip_command = "zip -r {} {}".format(target_name, source)
#zip_command = "zip -r {} {}".format(target_name, ''.join(source))

print(zip_command)
if os.system(zip_command) == 0:
    print('Success backup {}'.format(target_name))
else:
    print('Failed')
