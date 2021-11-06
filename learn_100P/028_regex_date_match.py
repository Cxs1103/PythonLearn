#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 028_regex_date_match.py
@Date  : 2021/11/6 0:39
@Author: Cxs
@Email: Cxs1103@163.com
<<<<<<< HEAD
@Desc  :
=======
@Desc  : 
>>>>>>> origin/master
'''

import re


def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date) is not None


date1 = "2021-11-06"
date2 = "2021/11-06"
date3 = "20211106"
date4 = "2021/11/06"
date5 = "2021aa1/06"

print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
print(date5, date_is_right(date5))
