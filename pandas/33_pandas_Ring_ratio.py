#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 33_pandas_Ring_ratio.py
@Date  : 2021/12/5 16:40
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas计算同比环比指标的3种方法
同比和环比：环比和同比用于描述统计数据的变化情况
环比：表示本次统计段与相连的上次统计段之间的比较。
比如2010年中国第一季度GDP为G2010Q1亿元，第二季度GDP为G2010Q2亿元，则第二季度GDP环比增长（G2010Q2-G2010Q1)/G2010Q1；
同比：即同期相比，表示某个特定统计段今年与去年之间的比较。
比如2009年中国第一季度GDP为G2009Q1亿元，则2010年第一季度的GDP同比增长为（G2010Q1-G2009Q1)/G2009Q1。
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/tongbi_huanbi.jpg

演示步骤：
读取连续3年的天气数据
方法1：pandas.Series.pct_change
方法2：pandas.Series.shift
方法3：pandas.Series.diff
pct_change、shift、diff，都实现了跨越多行的数据计算
'''
import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
import matplotlib.pyplot as plt

fpath = "./datas/beijing_tianqi_2017-2019.csv"
df = pd.read_csv(fpath, index_col="ymd", parse_dates=True)

print(df.head())

# 替换掉温度的后缀℃
df["bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')

print(df.head())

df = df[["bWendu"]].resample("M").mean()
print(df.head())

# 将索引按照日期升序排列
df.sort_index(ascending=True, inplace=True)

print(df.head())

print(df.index)

df.plot()
# plt.show()


# 方法1：pandas.Series.pct_change
# pct_change方法直接算好了"(新-旧)/旧"的百分比
# 官方文档地址：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pct_change.html
df["bWendu_way1_huanbi"] = df["bWendu"].pct_change(periods=1)
df["bWendu_way1_tongbi"] = df["bWendu"].pct_change(periods=12)

print(df.head())

# 方法2：pandas.Series.shift
# shift用于移动数据，但是保持索引不变
# 官方文档地址：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.shift.html

# 见识一下shift做了什么事情
# 使用pd.concat合并Series列表变成一个大的df
print(
    pd.concat(
        [df["bWendu"],
         df["bWendu"].shift(periods=1),
         df["bWendu"].shift(periods=12)],
        axis=1
    ).head(15)
)

# 环比
series_shift1 = df["bWendu"].shift(periods=1)
df["bWendu_way2_huanbi"] = (df["bWendu"] - series_shift1) / series_shift1

# 同比
series_shift2 = df["bWendu"].shift(periods=12)
df["bWendu_way2_tongbi"] = (df["bWendu"] - series_shift2) / series_shift2
print(df.head(15))

# 方法3. pandas.Series.diff
# pandas.Series.diff用于新值减去旧值
# 官方文档：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.diff.html
print(
    pd.concat(
        [df["bWendu"],
         df["bWendu"].diff(periods=1),
         df["bWendu"].diff(periods=12)],
        axis=1
    ).head(15)
)
# 环比
series_diff1 = df["bWendu"].diff(periods=1)
df["bWendu_way3_huanbi"] = series_diff1/(df["bWendu"]-series_diff1)

# 同比
series_diff2 = df["bWendu"].diff(periods=12)
df["bWendu_way3_tongbi"] = series_diff2/(df["bWendu"]-series_diff2)
print(df.head(15))