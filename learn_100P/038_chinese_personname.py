#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 038_chinese_personname.py
@Date  : 2021/11/6 16:35
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

with open("./datas/大奉打更人[www.xsbooktxt.cc].txt") as fin:
    content = fin.read()

import jieba.posseg as posseg

words = []
for word, flag in posseg.cut(content):
    # print(word, flag)
    if flag == 'nr':
        words.append(word)
# print(f'人名展示：',words)

import pandas as pd
print(pd.Series(words).value_counts()[:20])