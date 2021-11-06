#!/usr/bin/env python
# encoding: utf-8
'''
@File  : mysql_to_excel.py
@Date  : 2021/10/11 22:16
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pyhton 导出 Excel表格
'''

import pandas as pd
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123456',
    port = 3306,
    db = 'baq',
    charset = 'utf8'
)

df = pd.read_sql("""
    select * from baq_ryxx limit 10
""", con=conn)
df.to_excel("人员信息表.xlsx", index=False)

df = pd.read_sql("""
    select spdx, spsc , max(spdx), min(spdx), avg(spdx) 
    from baq_rygj_sp 
    group by spdx, spsc limit 10
""", con=conn).pivot(index="spdx", columns="spsc")
df.to_excel("视频时长信息表.xlsx")