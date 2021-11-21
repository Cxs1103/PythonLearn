#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 01_read_file.py
@Date  : 2021/11/20 23:53
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
'''

import pandas as pd
import pymysql

# csv文件路径
csv_path = "./datas/ratings.csv"

# 读取csv文件
ratings = pd.read_csv(csv_path)

# 查看前几行
print("CSV前几行数据：", '\n', ratings.head())

# 查看数据，返回（行数，列数）
print("CSV行数与列数：", '\n', ratings.shape)

# 查看索引
print("CSV索引：", '\n', ratings.index)

# 查看列名列表
print("CSV列名列表：", '\n', ratings.columns)

# 查看每列的数据类型
print("CSV每列的数据类型：", '\n', ratings.dtypes)

# csv文件路径
txt_path = "./datas/access_pvuv.txt"

# 读取txt文件,并添加列名
pv_uv = pd.read_csv(txt_path,
                    sep="\t",
                    header=None,
                    names=['pdate', 'pv', 'uv']
                    )

print("TXT数据：", '\n', pv_uv)

# excel文件路径
excel_path = "./datas/access_pvuv.xlsx"

# 读取excel文件
excel_file = pd.read_excel(excel_path)
print("Excel数据：", '\n', excel_file)

# 读取mysql文件
# 连接数据库
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='python_test',
    charset='utf8'
)

mysql_page = pd.read_sql("select * from crazyant_pvuv", con=conn)
print("MySQL数据：", '\n', mysql_page)
