#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 014_count_word.py
@Date  : 2021/11/4 22:10
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

word_count = {}

with open('./datas/014_file') as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

print(
    sorted(
        word_count.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
)
