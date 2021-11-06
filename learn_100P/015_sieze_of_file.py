#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 015_sieze_of_file.py
@Date  : 2021/11/4 22:46
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import os

print(os.path.getsize("/datas/014_file"))

sum_size = 0
for file in os.listdir('.'):
    if os.path.isfile(file):
        sum_size += os.path.getsize(file)

print("all size of dir :", sum_size / 1024)
