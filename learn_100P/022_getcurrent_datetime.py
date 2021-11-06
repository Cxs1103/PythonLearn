#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 022_getcurrent_datetime.py
@Date  : 2021/11/5 22:13
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import datetime

current_datetime = datetime.datetime.now()

print(current_datetime, type(current_datetime))

# date time to string
str_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(str_time)

print("Year :", current_datetime.year)
print("Month :", current_datetime.month)
print("Day :", current_datetime.day)
print("Hour :", current_datetime.hour)
print("Minute :", current_datetime.minute)
print("Second :", current_datetime.second)
