#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 016_arrange_file+bu_ext.py
@Date  : 2021/11/4 23:33
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import os
import shutil

dir = './datas/arrange_dir'

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)
