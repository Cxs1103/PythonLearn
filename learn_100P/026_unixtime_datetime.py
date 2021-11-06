#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 026_unixtime_datetime.py
@Date  : 2021/11/5 23:25
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import datetime

unixtime = 1636125917

datetime_obj = datetime.datetime.fromtimestamp(unixtime)
datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_obj, type(datetime_obj))
print(datetime_str, type(datetime_str))
