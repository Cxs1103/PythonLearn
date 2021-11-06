#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 017_search_dir.py
@Date  : 2021/11/4 23:53
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import os

search_dir = "D:\QMDownload"

result_files = []

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(".exe"):
            file_path = f"{root}/{file}"
            result_files.append((file_path, os.path.getsize(file_path) / 1024 / 1024))

print(
    sorted(result_files,
           key=lambda x: x[1],
           reverse=True)[:10]
)
