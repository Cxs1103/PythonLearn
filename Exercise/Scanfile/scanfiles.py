#!/usr/bin/env python
# encoding: utf-8
'''
@File  : scanfiles.py
@Date  : 2021/10/23 14:34
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python 查找文件夹中的指定文件
'''

import os
fount = open('./filename.txt', "w")

# 文件夹为数据要多加一个斜杠
for root, dirs, files in os.walk("D:\work\Weekly\\2021"):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        if file.endswith(".xlsx"):
            fount.write(file_path + "\n")

fount.close()