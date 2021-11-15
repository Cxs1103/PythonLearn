#!/usr/bin/env python
# encoding: utf-8
'''
@File  : rename.py
@Date  : 2021/11/15 21:38
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import os

os.chdir(r'./datas')
# print(os.listdir())
old_names = os.listdir(os.getcwd())
new_names = list(map(lambda x: x.replace('.txt', '.png'), old_names))

for old_name, new_name in zip(old_names, new_names):
    os.renames(old_name, new_name)
print('文件格式已经修改。。。。')
