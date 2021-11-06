#!/usr/bin/env python
# encoding: utf-8
'''
@File  : ExtractKeywords.py
@Date  : 2021/10/23 0:33
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python提取文章关键词
'''
import jieba.analyse

web_file = "./ExtractKeywords.txt"

def get_keyword_from_file(fname):
    with open(fname,encoding='utf-8') as fin:
        content = fin.read()
    return jieba.analyse.extract_tags(content,20)

print(get_keyword_from_file(web_file))