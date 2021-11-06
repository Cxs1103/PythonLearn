#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 036_split_file_get_words.py
@Date  : 2021/11/6 11:55
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import re
import pandas as pd

with open("./datas/036_split_file.txt") as fin:
    file_result = fin.read()

words = re.split(r"[\s.()-;!,?/""]+", file_result)

print(pd.Series(words).value_counts()[:20])
