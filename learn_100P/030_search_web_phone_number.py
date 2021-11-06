#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 030_search_web_phone_number.py
@Date  : 2021/11/6 1:08
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import re

pattern = r"1[3-9]\d{9}"

with open('./datas/030_web_phone_number') as fin:
    for line in fin:
        results = re.findall(pattern, line)
        for result in results:
            print(result)
