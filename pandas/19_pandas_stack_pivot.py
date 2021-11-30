#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 19_pandas_stack_pivot.py
@Date  : 2021/11/30 21:32
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas的stack和pivot实现数据透视
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/reshaping_example.png
经过统计得到多维度指标数据
使用unstack实现数据二维透视
使用pivot简化透视
stack、unstack、pivot的语法
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

# 1. 经过统计得到多维度指标数据
# 非常常见的统计场景，指定多个维度，计算聚合后的指标
# 实例：统计得到“电影评分数据集”，每个月份的每个分数被评分多少次：（月份、分数1~5、次数）

df = pd.read_csv(
    "./datas/movielens_1m/ratings.dat",
    header=None,
    names="UserID::MovieID::Rating::Timestamp".split("::"),
    sep="::",
    engine="python"
)
print(df.head())

df["pdate"] = pd.to_datetime(df["Timestamp"], unit='s')
print(df.head())
print(df.dtypes)

# 实现数据统计,先按照月份、评分进行分组，然后取出“UserID”聚合agg新的一列pv评分次数
df_group = df.groupby([df["pdate"].dt.month, "Rating"])["UserID"].agg(pv=np.size)
print(df_group.head(20))
# 对这样格式的数据，我想查看按月份，不同评分的次数趋势，是没法实现的
# 需要将数据变换成每个评分是一列才可以实现

# 2. 使用unstack实现数据二维透视
# 目的：想要画图对比按照月份的不同评分的数量趋势
df_stack = df_group.unstack()
print(df_stack)

df_stack.plot()
# plt.show()

# unstack和stack是互逆操作
df_stack.stack().head(20)

# 3. 使用pivot简化透视
print(df_group.head(20))

df_reset = df_group.reset_index()
print(df_reset.head())

df_pivot = df_reset.pivot("pdate", "Rating", "pv")
print(df_pivot.head())
df_pivot.plot()
plt.show()
# pivot方法相当于对df使用set_index创建分层索引，然后调用unstack

"""
4. stack、unstack、pivot的语法
stack：DataFrame.stack(level=-1, dropna=True)，将column变成index，类似把横放的书籍变成竖放
level=-1代表多层索引的最内层，可以通过==0、1、2指定多层索引的对应层
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/reshaping_stack.png

unstack：DataFrame.unstack(level=-1, fill_value=None)，将index变成column，类似把竖放的书籍变成横放
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/reshaping_unstack.png

pivot：DataFrame.pivot(index=None, columns=None, values=None)，指定index、columns、values实现二维透视
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/reshaping_pivot.png
"""