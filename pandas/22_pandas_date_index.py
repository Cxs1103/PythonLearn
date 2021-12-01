#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 22_pandas_date_index.py
@Date  : 2021/12/1 23:02
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎么处理日期索引的缺失？
问题：按日期统计的数据，缺失了某天，导致数据不全该怎么补充日期？

公众号：蚂蚁学Python

可以用两种方法实现：
1、DataFrame.reindex，调整dataframe的索引以适应新的索引
2、DataFrame.resample，可以对时间序列重采样，支持补充缺失值

问题：如果缺失了索引该怎么填充？
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "pdate": ["2019-12-01", "2019-12-02", "2019-12-04", "2019-12-05"],
    "pv": [100, 200, 400, 500],
    "uv": [10, 20, 40, 50]
})
print(df)

# df.set_index('pdate').plot()
# plt.show()

"""
问题，这里缺失了2019-12-03的数据，导致数据不全该怎么补充？
"""
# 方法1：使用pandas.reindex方法
# 1、将df的索引变成日期索引
df_date = df.set_index("pdate")
print(df_date)
print(df_date.index)

# 将df的索引设置为日期索引
df_date = df_date.set_index(pd.to_datetime(df_date.index))
print(df_date)
print(df_date.index)

# 2、使用pandas.reindex填充缺失的索引
# 生成完整的日期序列
pdates = pd.date_range(start="2019-12-01", end="2019-12-05")
print(pdates)

df_date_new = df_date.reindex(pdates, fill_value=0)
print(df_date_new)

# df_date_new.plot()
# plt.show()


# 方法2：使用pandas.resample方法
# 1、先将索引变成日期索引
print(df)

df_new2 = df.set_index(pd.to_datetime(df['pdate'])).drop('pdate', axis=1)
print(df_new2)
print(df_new2.index)

"""
2、使用dataframe的resample的方法按照天重采样
resample的含义：
改变数据的时间频率，比如把天数据变成月份，或者把小时数据变成分钟级别

resample的语法：
(DataFrame or Series).resample(arguments).(aggregate function)

resample的采样规则参数：
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

# 由于采样会让区间变成一个值，所以需要指定mean等采样值的设定方法
"""
df_new2 = df_new2.resample("D").mean().fillna(0)
print(df_new2)

# resample的使用方式
print(df_new2.resample("2D").mean())