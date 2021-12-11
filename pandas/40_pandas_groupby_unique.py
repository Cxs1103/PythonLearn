#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 40_pandas_groupby_unique.py
@Date  : 2021/12/11 15:37
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :

Pandas怎样实现groupby聚合后字符串列的合并
需求：
计算每个月的最高温度、最低温度、出现的风向列表、出现的空气质量列表


'''
# 数据输入

import pandas as pd

file_path = './datas/beijing_tianqi_2018.csv'
df = pd.read_csv(file_path)
print(df.head())

print(df.info())

# 知识：series怎样从str类型变成int
df["bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df["yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())

# 知识：进行日期列解析，可以方便提取月份
df["ymd"] = pd.to_datetime(df["ymd"])
print(df["ymd"].dt.month)

# 知识：series可以用Series.unique去重
print(df["fengxiang"].unique())

# 知识：可以用",".join(series)实现数组合并成大字符串
print(",".join(df["fengxiang"].unique()))

# 方法1
result = (
    df.groupby(df["ymd"].dt.month)
        .agg(
        # 新列名 = （原列名，函数）
        最高温=('bWendu', "max"),
        最低温=('yWendu', "min"),
        风向=('fengxiang', lambda x: ','.join(x.unique())),
        空气质量=('aqiInfo', lambda x: ','.join(x.unique())),
    )
        .reset_index()
        .rename(columns={"ymd": "月份"})
)

print(result)

# 方法2
def agg_func(x):
    """注意，这个x是每个分组的dataframe"""
    return pd.Series({
        "最高温度": x["bWendu"].max(),
        "最低温度": x["yWendu"].min(),
        "风向列表": ",".join(x["fengxiang"].unique()),
        "空气质量列表": ",".join(x["aqiInfo"].unique())
    })

result = df \
        .groupby(df["ymd"].dt.month) \
        .apply(agg_func) \
        .reset_index() \
        .rename(columns={"ymd":"月份"})
print(result)