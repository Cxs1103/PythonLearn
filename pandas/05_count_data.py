#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 05_count_data.py
@Date  : 2021/11/21 16:00
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas数据统计函数
汇总类统计
唯一去重和按值计数
相关系数和协方差
'''
import pandas as pd

df = pd.read_csv("./datas/beijing_tianqi_2018.csv")
print(df.head(6))

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head(3))

# 一下子提取所有数字列统计结果
print(df.dtypes)
print(df.describe())

# 查看单个Series的数据
print(df['bWendu'].mean())

# 最高温
print(df['bWendu'].max())

# 最低温
print(df['bWendu'].min())


"""
唯一去重和按值计数

唯一性去重:
一般不用于数值列，而是枚举、分类列
"""
print(df['fengxiang'].unique())
print(df['tianqi'].unique())
print(df['fengli'].unique())

# 按值计数
print(df['fengxiang'].value_counts())
print(df['fengli'].value_counts())

"""
相关系数和协方差
用途（超级厉害）：

两只股票，是不是同涨同跌？程度多大？正相关还是负相关？
产品销量的波动，跟哪些因素正相关、负相关，程度有多大？
来自知乎，对于两个变量X、Y：

协方差：衡量同向反向程度，如果协方差为正，说明X，Y同向变化，协方差越大说明同向程度越高；如果协方差为负，说明X，Y反向运动，协方差越小说明反向程度越高。
相关系数：衡量相似度程度，当他们的相关系数为1时，说明两个变量变化时的正向相似度最大，当相关系数为－1时，说明两个变量变化的反向相似度最大
"""
# 协方差矩阵：
print(df.cov())

# 相关系数矩阵
print(df.corr())

# 单独查看空气质量和最高温度的相关系数
print(df["aqi"].corr(df["bWendu"]))
print(df["aqi"].corr(df["yWendu"]))

# 空气质量和温差的相关系数
print(df["aqi"].corr(df["bWendu"]-df["yWendu"]))

# !! 这就是特征工程对于机器学习重要性的一个例子
print(0.21/0.02)