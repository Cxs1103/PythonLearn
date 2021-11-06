#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 034_search_phone_number_mosaic.py
@Date  : 2021/11/6 11:11
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import re

content = """
    除1986年因是15869862037实行夏令时的第一年，13052522525从5月4日开始到9月14日结束外，其它年份18917175643均按规定的时11111111段施行。夏令时实12345678901施期间，将时间向后调快一小时。1992年4月5日后不再实行。
"""

patternt = r"(1[3-9]{1}[0-9]{1})(\d{4})(\d{4})"

print(re.sub(patternt, r"\1****\3", content))
