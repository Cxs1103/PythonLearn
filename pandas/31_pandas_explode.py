#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 31_pandas_explode.py
@Date  : 2021/12/5 14:00
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas使用explode实现一行变多行统计
解决实际问题：一个字段包含多个值，怎样将这个值拆分成多行，然后实现统计

比如：一个电影有多个分类、一个人有多个喜好，需要按分类、喜好做统计
'''
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

df = pd.read_csv(
    "./datas/movielens_1m/movies.dat",
    header=None,
    names="MovieID::Title::Genres".split("::"),
    sep="::",
    engine="python"
)
print(df.head())

"""
问题：怎样实现这样的统计，每个题材有多少部电影？

解决思路：
将Genres按照分隔符|拆分
按Genres拆分成多行
统计每个Genres下的电影数目
"""

# 2、将Genres字段拆分成列表
print(df.info())

# 当前的Genres字段是字符串类型
print(type(df.iloc[0]["Genres"]))

# 新增一列
df["Genre"] = df["Genres"].map(lambda x: x.split("|"))
print(df.head())

# Genre的类型是列表
print(df["Genre"][0])
print(type(df["Genre"][0]))
print(df.info())

# 3、使用explode将一行拆分成多行
# 语法：pandas.DataFrame.explode(column)
# 将dataframe的一个list-like的元素按行复制，index索引随之复制
df_new = df.explode("Genre")
print(df_new.head(10))

# 4、实现拆分后的题材的统计
df_new["Genre"].value_counts().plot.bar()
# df_new["Genre"].value_counts().plot()
plt.show()