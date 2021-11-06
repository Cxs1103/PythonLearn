#!/usr/bin/env python
# encoding: utf-8
'''
@File  : mysql_to_excel.py
@Date  : 2021/10/11 22:16
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :Python批量存储数据到MySQL
'''

import pandas as pd
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    port=3306,
    db='students',
    charset='utf8'
)

df = pd.read_excel("学生成绩表.xlsx")
for idx, row in df.iterrows():
    print(f"process:{row.student_name}, {row.yuwen}")
    # student_name = row.student_name.encode("utf-8").decode("latin1")
    sql = f"""
        insert into students
        (student_name, yuwen, shuxue, yingyu)
        values ('{row.student_name}', '{row.yuwen}', '{row.shuxue}', '{row.yingyu}')
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

cursor.close()
