#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 020_concat_text_files.py
@Date  : 2021/11/5 21:06
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 合并多个文件
'''

import os

data_dir = "./datas/many_texts"

contents = []
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path) as fin:
            contents.append(fin.read())

final_content = "\n".join(contents)

with open("./datas/many_texts/many_texts.txt", "w") as fout:
    fout.write(final_content)
