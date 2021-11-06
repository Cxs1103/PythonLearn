#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 011_sort_student_list.py
@Date  : 2021/11/3 22:40
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

students = [
    {"sno": 101, "name": "zhangsan", "sgrade": 88},
    {"sno": 102, "name": "lisi", "sgrade": 85},
    {"sno": 103, "name": "wangwu", "sgrade": 47},
    {"sno": 104, "name": "zhaoliu", "sgrade": 100},
]

students_sort = sorted(students, key=lambda x: x["sgrade"])
print(students)
print(students_sort)

students_sort = sorted(students, key=lambda x: x["sgrade"], reverse=True)
print(students_sort)
