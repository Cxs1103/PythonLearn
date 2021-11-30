#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 20_pandas_apply.py
@Date  : 2021/11/30 23:18
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas使用apply函数给表格添加多列
'''
import pandas as pd

df = pd.read_csv("./datas/beijing_tianqi_2017-2019.csv")
print(df.head())

# 温度形式转换为数字
df['bWendu'] = df["bWendu"].map(lambda x: int(str(x).replace("℃", "")))
df['yWendu'] = df["yWendu"].map(lambda x: int(str(x).replace("℃", "")))

print(df.head())
"""
# 添加一列
def my_func(row):
    new_column = row['a'] + row['b']
    return new_column

df["new_column"] = df.apply(my_func, axis=1)
"""


# 添加多列，添加温差和平均温度
def my_func(row):
    return row["bWendu"] - row["yWendu"], (row['bWendu'] + row['yWendu']) / 2

df[["wencha", "avg"]] = df.apply(my_func, axis=1, result_type="expand")
print(df.head())