#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 15_pandas_groupby.py
@Date  : 2021/11/28 17:32
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎样实现groupby分组统计
类似SQL：
select city,max(temperature) from city_weather group by city;

groupby：先对数据分组，然后在每个分组上应用聚合函数、转换函数

本次演示：
一、分组使用聚合函数做数据统计
二、遍历groupby的结果理解执行流程
三、实例分组探索天气数据
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print(df)

# 一、分组使用聚合函数做数据统计
# 1、单个列groupby，查询所有数据列的统计
print(df.groupby('A').sum())

"""
groupby中的'A'变成了数据的索引列
因为要统计sum，但B列不是数字，所以被自动忽略掉
"""
# 2、多个列groupby，查询所有数据列的统计
print(df.groupby(['A', 'B']).mean())
# 我们看到：('A','B')成对变成了二级索引

print(df.groupby(['A', 'B'], as_index=False).mean())

# 3、同时查看多种数据统计
print(df.groupby('A').agg([np.sum, np.mean, np.std]))
# 我们看到：列变成了多级索引

# 4、查看单列的结果数据统计
# 方法1：预过滤，性能更好
print(df.groupby('A')['C'].agg([np.sum, np.mean, np.std]))
print(df.groupby('A')['D'].agg([np.sum, np.mean, np.std]))

# 方法2
print(df.groupby('A').agg([np.sum, np.mean, np.std])['C'])
print(df.groupby('A').agg([np.sum, np.mean, np.std])['D'])

# 不同列使用不同的聚合函数
print(df.groupby('A').agg({'C': np.sum, "D": np.mean}))

"""
二、遍历groupby的结果理解执行流程
for循环可以直接遍历每个group
"""
# 1、遍历单个列聚合的分组
g = df.groupby('A')
print(g)
for name, group in g:
    print(name)
    print(group)

# 可以获取单个分组的数据
print(g.get_group('foo'))

# 2、遍历多个列聚合的分组
g = df.groupby(['A', 'B'])
print(g)
for name, group in g:
    print(name)
    print(group)
    print()
# 可以看到，name是一个2个元素的tuple，代表不同的列
print(g.get_group(('foo', 'one')))

# 可以直接查询group后的某几列，生成Series或者子DataFrame
print(g['C'])

for name, group in g['C']:
    print(name)
    print(group)
    print(type(group))
    print()
# 其实所有的聚合统计，都是在dataframe和series上进行的；


# 三、实例分组探索天气数据

fpath = './datas/beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())

# 新增一列分组
df['month'] = df['ymd'].str[:7]
print(df.head())

# 查看每个月的最高气温
data = df.groupby('month')['bWendu'].max()
print(data)
print(type(data))

data.plot()
# plt.show()

# 2、查看每个月的最高温度、最低温度、平均空气质量指数
print(df.head())

group_data = df.groupby('month').agg({'bWendu': np.max, 'yWendu': np.min, 'aqi': np.mean})
print(group_data)
group_data.plot()
plt.show()