#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 024_date_diff_days.py
@Date  : 2021/11/5 22:41
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import datetime

def get_date_diff_days(pdate,days):
    pdate_obj = datetime.datetime.strptime(pdate,'%Y-%m-%d')
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime("%Y-%m-%d")

print(get_date_diff_days("2021-10-5",2))
print(get_date_diff_days("2021-11-5",6))
print(get_date_diff_days("2021-11-5",1))
print(get_date_diff_days("2021-10-28",2))
print(get_date_diff_days("2021-10-15",2))