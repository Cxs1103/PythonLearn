#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 26_pandas_logs.py
@Date  : 2021/12/4 13:52
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas处理分析网站原始访问日志
目标：真实项目的实战，探索Pandas的数据处理与分析

实现步骤：
1、读取数据、清理、格式化
2、统计爬虫spider的访问比例，输出柱状图
3、统计http状态码的访问占比，输出饼图
4、统计按小时、按天的PV/UV流量趋势，输出折线图
'''

import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Line
import os

pd.set_option('display.max_colwidth', -1)

# 读取整个目录，将所有的文件合并到一个dataframe
data_dir = './datas/logs'
df_list = []

for fname in os.listdir(f"{data_dir}"):
    df_list.append(pd.read_csv(f"{data_dir}/{fname}", sep=" ", header=None, error_bad_lines=False))

df = pd.concat(df_list)
print(df.head())

df = df[[0, 3, 6, 9]].copy()
print(df.head())

df.columns = ['ip', 'stime', 'status', 'client']
print(df.head())
print(df.dtypes)

# 2、统计spider的比例
df['is_spider'] = df["client"].str.lower().str.contains("spider")
print(df.head())

df_spider = df["is_spider"].value_counts()
print(df_spider)

bar = (
    Bar()
        .add_xaxis([str(x) for x in df_spider.index])
        .add_yaxis("是否是Spider", df_spider.values.tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title="爬虫访问量"))
)
bar.render('./datas/logs/spider_request_count.html')

# 3、访问状态码的数量对比
df_status = df.groupby("status").size()
print(df_status)

print(list(zip(df_status.index, df_status)))

pie = (
    Pie()
        .add("状态对比", list(zip(df_status.index, df_status)))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)
pie.render('./datas/logs/spider_status.html')

# 4、实现按小时、按天粒度的流量统计
print(df.head())

df['stime'] = pd.to_datetime(df['stime'].str[1:], format="%d/%b/%Y:%H:%M:%S")
print(df.head())

df.set_index("stime", inplace=True)
df.sort_index(inplace=True)
print(df.head())
print(df.index)

# 按小时统计
# df_pvuv = df.resample('H')['ip'].agg(pv=np.size, uv=pd.Series.nunique)

# 按每6个小时统计
# df_pvuv = df.resample("6H")["ip"].agg(pv=np.size, uv=pd.Series.nunique)

# 按天统计
df_pvuv = df.resample("D")["ip"].agg(pv=np.size, uv=pd.Series.nunique)

print(df_pvuv.head())

line = (
    Line()
    .add_xaxis(df_pvuv.index.to_list())
    .add_yaxis("PV", df_pvuv['pv'].to_list())
    .add_yaxis("UV", df_pvuv['uv'].to_list())
    .set_global_opts(
        title_opts=opts.TitleOpts(title='PVUV数据对比'),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
    )
)
line.render('./datas/logs/spider_pvuv.html')
