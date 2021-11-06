#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 021_student_like_count.py
@Date  : 2021/11/5 21:54
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

student_like_count = {}

with open('./datas/student_like.txt', encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]
        sname, slike = line.split(" ")
        like_list = slike.split(",")
        for like in like_list:
            if like not in student_like_count:
                student_like_count[like] = 0
            student_like_count[like] += 1
    print(student_like_count)
