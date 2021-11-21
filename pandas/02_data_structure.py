#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 02_data_structure.py
@Date  : 2021/11/21 10:51
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import pandas as pd
import numpy as np

# 创建Series
# Series是一种类似于一维数组的对象，它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成。
s1 = pd.Series([1, 'a', 5.2, 7])

# 输出Series
print(s1)

# 输出Series index
print(s1.index)

# 输出Series value
print(s1.values)

# 创建一个具有标签索引的Series
s2 = pd.Series([1, 'a', 5.2, 7], index=['d', 'b', 'a', 'c'])

print(s2)

print(s2.index)

# 使用Python字典创建Series
sdata = {'Ohio': 35000, 'Texas': 7200, 'Oregon': 16000, 'Uath': 5000}

s3 = pd.Series(sdata)
print(s3)

# 根据标签索引查询数据
print(s2)

print(s2['a'])
print(type(s2['a']))

print(s2[['b', 'a']])
print(type(s2[['b', 'a']]))

"""
DataFrame是一个表格型的数据结构:
1.每列可以是不同的值类型（数值、字符串、布尔值等）
2.既有行索引index,也有列索引columns
3.可以被看做由Series组成的字典
"""
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print(df.columns)
print(df.index)

"""
从DataFrame中查询出Series:
1.如果只查询一行、一列，返回的是pd.Series
2.如果查询多行、多列，返回的是pd.DataFrame
"""

print(df)
print(df['year'])
type(df['year'])

# 查询多列，结果是一个pd.DataFrame
print(df[['year', 'pop']])
print(type(df[['year', 'pop']]))

# 查询一行，结果是一个pd.Series
print(df.loc[1])
print(type(df.loc[1]))

# 查询多行，结果是一个pd.DataFrame
print(df.loc[1:3])
print(type(df.loc[1:3]))
