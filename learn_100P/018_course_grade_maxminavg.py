#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 018_course_grade_maxminavg.py
@Date  : 2021/11/5 0:10
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

# key:course  ,value: grade list
course_grades = {}

with open('./datas/018_grade_file') as fin:
    for line in fin:
        course, sno, sname, grade = line.split(',')
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(grade))

print(course_grades)

for course, grades in course_grades.items():
    print(
        course, max(grades), min(grades), sum(grades) / len(grades)
    )
