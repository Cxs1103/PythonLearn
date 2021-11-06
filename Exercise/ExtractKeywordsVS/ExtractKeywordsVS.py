#!/usr/bin/env python
# encoding: utf-8
'''
@File  : ExtractKeywords.py
@Date  : 2021/10/23 0:33
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python提取文章关键词，并进行对比，类似于论文查重
'''
import jieba.analyse

web_file0 = "./ExtractKeywords.txt"
web_file1 = "./ExtractKeywords01.txt"

def get_keyword_from_file(fname):
    with open(fname,encoding='utf-8') as fin:
        content = fin.read()
    return jieba.analyse.extract_tags(content,20)

def compute_sim(wordsa, wordsb):
    jiaoji = set(wordsa).intersection(set(wordsb))
    bingji = set(wordsa).union(set(wordsb))
    return round(len(jiaoji) * 100 / len(bingji), 2)

web_file_words0 = get_keyword_from_file(web_file0)
web_file_words1 = get_keyword_from_file(web_file1)

print("web_file0 vs web_file0", compute_sim(web_file_words0, web_file_words0))
print("web_file0 vs web_file1", compute_sim(web_file_words0, web_file_words1))