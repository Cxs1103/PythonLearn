#!/usr/bin/env python
# encoding: utf-8
'''
@File  : ExclesVlookup.py
@Date  : 2021/10/25 0:37
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python实现多个Excel表的vlookup
'''

import xlwings as xw
import pandas as pd
import os

app = xw.App(visible=False, add_book=False)

workbook = app.books.open("成绩表数据.xlsx")

# 读取“总表”
df_total = (
    workbook
    .sheets[0]
    .range("A1")
    .options(pd.DataFrame, expand='table', index=False, numbers=int)
    .value)
# print(df_total)

# 读取各个班级的学生数据
df_student_list = []
for file_name in os.listdir("学生信息"):
    if "同学录" not in file_name:
        continue

    workbook_student = app.books.open("学生信息/" + file_name)

    df_student = (
        workbook_student
        .sheets[0]
        .range("A1")
        .options(pd.DataFrame, expand='table', index=False, numbers=int)
        .value)

    df_student["班级"] = file_name.replace("同学录.xlsx", "")
    df_student_list.append(df_student)

    workbook_student.close()
    # print(df_student_list)
df_student_all = pd.concat(df_student_list)
# print(df_student_all)

df_merge = pd.merge(left=df_total, right=df_student_all, left_on=["班级", "姓名"], right_on=["班级", "姓名"])
# print(df_merge)

df_merge["电话号码"] = df_merge["电话"]
df_merge.drop(columns="电话", inplace=True)
# print(df_merge)

workbook.sheets[0].range("A1").options(index=False).value=df_merge
workbook.save()
workbook.close()

app.quit()