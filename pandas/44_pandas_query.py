#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 44_pandas_query.py
@Date  : 2021/12/12 0:24
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas查询数据的简便方法df.query
怎样进行复杂组合条件对数据查询：

方式1. 使用df[(df["a"] > 3) & (df["b"]<5)]的方式；
方式2. 使用df.query("a>3 & b<5")的方式；
方法2的语法更加简洁

性能对比：

当数据量小时，方法1更快；
当数据量大时，因为方法2直接用C语言实现，节省方法1临时数组的多次复制，方法2更快；
'''

import pandas as pd

print(pd.__version__)

# 0、读取数据
# 数据为北京2018年全年天气预报

df = pd.read_csv("./datas/beijing_tianqi_2018.csv")
print(df.head())

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())

# 1、使用dataframe条件表达式查询
# 最低温度低于-10度的列表
print(df[df['yWendu'] < -10])

# 复杂条件查询
# 注意，组合条件用&符号合并，每个条件判断都得带括号

## 查询最高温度小于30度，并且最低温度大于15度，并且是晴天，并且天气为优的数据
print(df[(df['bWendu'] < 30) & (df['yWendu'] > 15)].head())
print(df[(df['bWendu'] < 30) & (df['yWendu'] > 15) & (df['tianqi'] == '晴')].head())
print(df[(df['bWendu'] < 30) & (df['yWendu'] > 15) & (df['tianqi'] == '晴') & (df['aqiLevel'] == 1)].head())

"""
2、使用df.query可以简化查询
形式：DataFrame.query(expr, inplace=False, **kwargs)

其中expr为要返回boolean结果的字符串表达式

形如：

df.query('a<100')
df.query('a < b & b < c')，或者df.query('(a<b)&(b<c)')
df.query可支持的表达式语法：

逻辑操作符: &, |, ~
比较操作符: <, <=, ==, !=, >=, >
单变量操作符: -
多变量操作符: +, -, *, /, %
df.query中可以使用@var的方式传入外部变量

df.query支持的语法来自NumExpr，地址：
https://numexpr.readthedocs.io/projects/NumExpr3/en/latest/index.html
"""
# 查询最低温度低于-10度的列表
print(df.query('yWendu < -10').head())

# 查询最高温度小于30度，并且最低温度大于15度，并且是晴天，并且天气为优的数据
print(df.query("bWendu < 30 & yWendu > 15 & tianqi == '晴' & aqiLevel == 1"))

# 查询温差大于15度的日子
print(df.query("bWendu - yWendu >15"))

# 可以使用外部的变量
# 查询温度在这两个温度之间的数据
high_temperature = 15
low_temperature = 13

print(df.query("yWendu <= @high_temperature & yWendu >= @low_temperature"))
