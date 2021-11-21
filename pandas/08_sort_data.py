#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 08_sort_data.py
@Date  : 2021/11/21 18:17
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas数据排序
Series的排序：
Series.sort_values(ascending=True, inplace=False)
参数说明：

ascending：默认为True升序排序，为False降序排序
inplace：是否修改原始Series
DataFrame的排序：
DataFrame.sort_values(by, ascending=True, inplace=False)
参数说明：

by：字符串或者List，单列排序或者多列排序
ascending：bool或者List，升序还是降序，如果是list对应by的多列
inplace：是否修改原始DataFrame
'''
import pandas as pd

# 读取数据
fpath = "./datas/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())

print(df['aqi'].sort_values())
print(df['aqi'].sort_values(ascending=False))

print(df["tianqi"].sort_values())

# DataFrame的排序
# 单列排序,升序
print(df.sort_values(by='aqi'))
# 单列排序,降序
print(df.sort_values(by='aqi', ascending=False))

# 多列排序
# 按空气质量等级、最高温度排序，默认升序
print(df.sort_values(by=["aqiLevel", "bWendu"]))

# 按空气质量等级、最高温度排序，降序
print(df.sort_values(by=["aqiLevel", "bWendu"], ascending=False))

# 分别指定升序和降序
print(df.sort_values(by=["aqiLevel", "bWendu"], ascending=[True, False]))