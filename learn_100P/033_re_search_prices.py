#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 033_re_search_prices.py
@Date  : 2021/11/6 10:54
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

content = """
    购物清单：
    2斤萝卜花了8元
    3斤柚子花了12.30元
    1斤牛肉花了35.6元
"""

import re

for line in content.split("\n"):
    pattern = r"(\d)斤(.*)花了(\d+(\.\d+)?)元"
    match = re.search(pattern, line)
    if match:
        print(f"{match.group(1)}\t{match.group(2)}\t{match.group(3)}")
