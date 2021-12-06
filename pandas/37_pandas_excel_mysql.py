#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 37_pandas_excel_mysql.py
@Date  : 2021/12/6 22:39
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Python使用Pandas将Excel存入MySQL
一个典型的数据处理流：

Pandas从多方数据源读取数据，比如excel、csv、mysql、爬虫等等
Pandas对数据做过滤、统计分析
Pandas将数据存储到MySQL，用于Web页面展示、后续的进一步SQL分析等等
官网文档：
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql
'''

import pandas as pd

df = pd.read_excel('./datas/vlookup/学生信息表.xlsx')
print(df.head())

# 展示索引的name
df.index.name = "id"
print(df.head())

"""
创建sqlalchemy对象连接MySQL
SQLAlchemy是Python中的ORM框架， Object-Relational Mapping，把关系数据库的表结构映射到对象上。

官网：https://www.sqlalchemy.org/
如果sqlalchemy包不存在，用这个命令安装：pip install sqlalchemy
需要安装依赖Python库：pip install mysql-connector-python
可以直接执行SQL语句
"""
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/test", echo=False)

# 方法1：当数据表不存在时，每次覆盖整个表
# 每次运行会drop table，新建表
df.to_sql(name='student', con=engine, if_exists="replace")

print(engine.execute("show create table student").first()[1])

print(engine.execute("select count(1) from student").first())

print(engine.execute("select * from student limit 5").fetchall())

# 方法2：当数据表存在时，每次新增数据
# 场景：每天会新增一部分数据，要添加到数据表，怎么处理？
df_new = df.loc[:4, :]
print(df_new)

df_new.to_sql(name='student', con=engine, if_exists='append')

print(engine.execute("select * from student where id<5").fetchall())

# 问题解决：先根据数据KEY删除旧数据
print(df_new.index)
for id in df_new.index:
    # 先删除要新增的数据
    delete_sql = f"delete from student where id={id}"
    print(delete_sql)
    engine.execute(delete_sql)

print(engine.execute("select * from student where id<5").fetchall())

print(engine.execute("select count(1) from student").first())

# 新增数据到表中
df_new.to_sql(name='student', con=engine, if_exists="append")
print(engine.execute("SELECT * FROM student where id<5 ").fetchall())

print(engine.execute("SELECT count(1) FROM student").first())