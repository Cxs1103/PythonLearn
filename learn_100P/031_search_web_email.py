#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 031_search_web_email.py
@Date  : 2021/11/6 1:15
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import re

pattern = re.compile(r"""
        [a-zA-Z0-9_-]+
        @
        [a-zA-Z0-9]+
        \.
        [a-zA-Z]{2,4}
    """, re.VERBOSE)

with open('./datas/031_web_email.txt') as fin:
    file_count = fin.read()

    results = pattern.findall(file_count)
    for result in results:
        print(result)