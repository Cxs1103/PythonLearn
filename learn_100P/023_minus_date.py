#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 023_minus_date.py
@Date  : 2021/11/5 22:21
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import datetime

birthday = "1995-12-24"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_date, type(birthday_date))

curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))

minus_datetime = curr_datetime - birthday_date
print(minus_datetime, type(minus_datetime))

print(minus_datetime.days)
print(round(minus_datetime.days / 365, 2))
