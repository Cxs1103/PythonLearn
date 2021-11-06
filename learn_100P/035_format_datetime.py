#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 035_format_datetime.py
@Date  : 2021/11/6 11:26
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import re

content = """
    时间格式：dd/MM/yyyy    06/03/2007
    时间格式：yyyy.MM.dd	2007.06.03
    时间格式：yyyy/MM/dd	2007/06/03
    时间格式：MM/dd/yyyy	3/06/2007
"""

content = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", content)
print(content)
content = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})", r"\1-\2-\3", content)
print(content)
content = re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\1-\2-\3", content)
print(content)
content = re.sub(r"(\d{1})/(\d{2})/(\d{4})", r"\3-\2-0\1", content)
print(content)