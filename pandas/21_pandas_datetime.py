#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 21_pandas_datetime.py
@Date  : 2021/12/1 21:16
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎样快捷方便的处理日期数据
Pandas日期处理的作用：将2018-01-01、1/1/2018等多种日期格式映射成统一的格式对象，在该对象上提供强大的功能支持

几个概念：
pd.to_datetime：pandas的一个函数，能将字符串、列表、series变成日期形式
Timestamp：pandas表示日期的对象形式
DatetimeIndex：pandas表示日期的对象列表形式

其中：
DatetimeIndex是Timestamp的列表形式
pd.to_datetime对单个日期字符串处理会得到Timestamp
pd.to_datetime对日期字符串列表处理会得到DatetimeIndex


问题：怎样统计每周、每月、每季度的最高温度？
'''
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series


# 1、读取天气数据到dataframe
fpath = './datas/beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())

# 2、将日期列转换成pandas的日期
df.set_index(pd.to_datetime(df['ymd']), inplace=True)
print(df.head())
print(df.index)

# DatetimeIndex是Timestamp的列表形式
print(df.index[0])

# 3、 方便的对DatetimeIndex进行查询
# 筛选固定的某一天
print(df.loc['2018-01-05'])

# 日期区间
print(df.loc['2018-01-05':'2018-01-10'])

# 按月份前缀筛选
print(df.loc['2018-03'])

# 按月份前缀筛选
print(df.loc['2018-07':'2018-09'].index)

# 按年份前缀筛选
print(df.loc['2018'].head())

print('===============================')
# 4、方便的获取周、月、季度
# Timestamp、DatetimeIndex支持大量的属性可以获取日期分量：
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components

# 周数字列表
# print(df.index.week)
print(pd.DatetimeIndex(df.index).isocalendar().week)

# 月数字列表
# print(df.index.month)
print(pd.DatetimeIndex(df.index).month)

# 季度数字列表
# print(df.index.quarter)
print(pd.DatetimeIndex(df.index).quarter)

# 5、统计每周、每月、每个季度的最高温度
# 统计每周的数据
print(df.groupby(pd.DatetimeIndex(df.index).isocalendar().week)["bWendu"].max().head())

# df.groupby(pd.DatetimeIndex(df.index).isocalendar().week)["bWendu"].max().plot()
# plt.show()

# 统计每个月的数据
print(df.groupby(df.index.month)["bWendu"].max())

# df.groupby(df.index.month)["bWendu"].max().plot()
# plt.show()

# 统计每个季度的数据
print(df.groupby(df.index.quarter)["bWendu"].max())
df.groupby(df.index.quarter)["bWendu"].max().plot()
plt.show()