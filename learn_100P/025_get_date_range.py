#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 025_get_date_range.py
@Date  : 2021/11/5 22:54
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import datetime


def get_date_range(begin_date, end_date):
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date_obj = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        day1_timedelta = datetime.timedelta(days=1)
        begin_date = (begin_date_obj + day1_timedelta).strftime("%Y-%m-%d")
    return date_list

begin_date = "2021-11-05"
end_date = "2021-11-15"
date_list = get_date_range(begin_date, end_date)
print(date_list)