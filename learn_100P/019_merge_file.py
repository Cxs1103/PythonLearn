#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 019_merge_file.py
@Date  : 2021/11/5 0:24
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
course_teacher_map = {}

with open("./datas/019_course_teacher") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(',')
        course_teacher_map[course] = teacher

print(course_teacher_map)

with open("./datas/018_grade_file") as fin:
    for line in fin:
        course, sno, sname, sgrade = line.split(',')
        teacher = course_teacher_map.get(course)
        print(course, teacher, sno, sname, sgrade)
