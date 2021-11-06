#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 029_search_all_phone_number.py
@Date  : 2021/11/6 0:57
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

content = """
    除1986年因是15869862037实行夏令时的第一年，13052522525从5月4日开始到9月14日结束外，其它年份18917175643均按规定的时11111111段施行。夏令时实12345678901施期间，将时间向后调快一小时。1992年4月5日后不再实行。
"""

import re

pattern = r"1[3-9]\d{9}"

results = re.findall(pattern, content)

for result in results:
    print(result)
