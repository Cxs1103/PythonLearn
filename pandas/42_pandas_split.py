#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 42_pandas_split.py
@Date  : 2021/12/11 22:32
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas处理Excel一列变多列
'''
# 1. 读取数据
import pandas as pd

df = pd.read_excel('./datas/split_onecolumn_tomany/学生数据表.xlsx')
print(df.head())


def split_func(line):
    line["姓名"], line["性别"], line["年龄"], line["城市"] = line["数据"].split(":")
    return line


# 2. 实现拆分
df = df.apply(split_func, axis=1)
print(df.head())

# 3. 删除多余原数据
df.drop(["数据"], axis=1, inplace=True)
print(df.head())

# 4. 输出到结果Excel
df.to_excel("./datas/split_onecolumn_tomany/学生数据表_拆分后.xlsx", index=False)
