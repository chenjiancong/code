#!/usr/bin/env python
# encoding: utf-8

<<<<<<< HEAD
import os
import time
=======
import time
import os
>>>>>>> 0e1aba716ad060c7c6b801946c029270da9d17eb

# source
source = ['/home/jack/test1']
# target_dir
target_dir = '/home/jack'
<<<<<<< HEAD
# make directory
today = target_dir + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(today):
    os.mkdir(today)
    print('Make directory: {}'.format(today))
=======
# today
today = target_dir + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(today):
    os.mkdir(today)
    print('Success make dirctory {}'.format(today))
# now
>>>>>>> 0e1aba716ad060c7c6b801946c029270da9d17eb
now = time.strftime('%H%M%S')
# target_name
target_name = today + os.sep + now + '.zip'
# zip_command
zip_command = 'zip -qr {} {}'.format(target_name, ''.join(source))

print(zip_command)
if os.system(zip_command) == 0:
<<<<<<< HEAD
    print('Success backup {}'.format(target_name))
else:
    print('Failed')


=======
    print('Sucess make backup file {}'.format(target_name))
else:
    print('Failed')
>>>>>>> 0e1aba716ad060c7c6b801946c029270da9d17eb
