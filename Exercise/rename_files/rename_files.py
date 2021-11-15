#!/usr/bin/env python
# encoding: utf-8
'''
@File  : rename_files.py
@Date  : 2021/11/15 22:16
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import os
import re

os.chdir(r'./datas')
old_names = os.listdir(os.getcwd())
# print(old_names)

def file_rename(text):
    contexts = re.findall(r'[\u4e00-\u9fa5]', text)
    return ''.join(contexts) + '.txt'

new_names = list(map(file_rename, old_names))

for old_name, new_name in zip(old_names, new_names):
    os.rename(old_name, new_name)
