#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 027_sale_data_week_diff.py
@Date  : 2021/11/6 0:05
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import datetime

date_sale = {}
is_first_line = True
with open('./datas/date_sale_data.txt') as fin:
    for line in fin:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date, sale_number = line.split("\t")
        date_sale[date] = float(sale_number)


def get_diff_days(date, days):
    curr_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    timedelta = datetime.timedelta(days=-days)
    return (curr_date + timedelta).strftime("%Y-%m-%d")


for date, sale_number in date_sale.items():
    date7 = get_diff_days(date, 7)
    sale_number7 = date_sale.get(date7, 0)
    if sale_number7 == 0:
        print(date, sale_number, 0)
    else:
        week_diff = (sale_number - sale_number7) / sale_number7
        print(date, sale_number, date7, sale_number7, week_diff)
