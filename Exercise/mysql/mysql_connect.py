#!/usr/bin/env python
# encoding: utf-8
'''
@File  : mysql_connect.py
@Date  : 2021/10/11 22:04
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123456',
    port = 3306,
    charset = 'utf8'
)

cursor = conn.cursor()
cursor.execute("select version()")
print(cursor.fetchone())