#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 16_pandas_multiIndex.py
@Date  : 2021/11/28 19:19
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas的分层索引MultiIndex
为什么要学习分层索引MultiIndex？

分层索引：在一个轴向上拥有多个索引层级，可以表达更高维度数据的形式；
可以更方便的进行数据筛选，如果有序则性能更好；
groupby等操作的结果，如果是多KEY，结果是分层索引，需要会使用
一般不需要自己创建分层索引(MultiIndex有构造函数但一般不用)
演示数据：百度、阿里巴巴、爱奇艺、京东四家公司的10天股票数据
数据来自：英为财经
https://cn.investing.com/

本次演示提纲：
一、Series的分层索引MultiIndex
二、Series有多层索引怎样筛选数据？
三、DataFrame的多层索引MultiIndex
四、DataFrame有多层索引怎样筛选数据？
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

stocks = pd.read_excel('./datas/互联网公司股票.xlsx')
print(stocks.head())
print(stocks.shape)
print(stocks["公司"].unique())
print(stocks.index)
print(stocks.groupby('公司')['收盘'].mean())

# 一、Series的分层索引MultiIndex
ser = stocks.groupby(['公司', '日期'])['收盘'].mean()
print(ser)
# 多维索引中，空白的意思是：使用上面的值
print(ser.index)

# unstack把二级索引变成列
print(ser.unstack())

# 修改原来索引
print(ser)
print(ser.reset_index())

# 二、Series有多层索引MultiIndex怎样筛选数据？
print(ser)

print(ser.loc['BIDU'])

# 多层索引，可以用元组的形式筛选
print(ser.loc[('BIDU', '2019-10-02')])

# 查看所公司2019-10-02的收盘数据
print(ser.loc[:, '2019-10-02'])

# 三、DataFrame的多层索引MultiIndex
print(stocks.head())

stocks.set_index(['公司', '日期'], inplace=True)
print(stocks)
print(stocks.index)

# 根据索引进行排序
stocks.sort_index(inplace=True)
print(stocks)

"""
四、DataFrame有多层索引MultiIndex怎样筛选数据？
【重要知识】在选择数据时：

元组(key1,key2)代表筛选多层索引，其中key1是索引第一级，key2是第二级，比如key1=JD, key2=2019-10-02
列表[key1,key2]代表同一层的多个KEY，其中key1和key2是并列的同级索引，比如key1=JD, key2=BIDU
"""
print(stocks.loc['BIDU'])

print(stocks.loc[('BIDU', '2019-10-02'), :])
print(stocks.loc[('BIDU', '2019-10-02'), '开盘'])
print(stocks.loc[['BIDU', 'JD'], :])
print(stocks.loc[(['BIDU', 'JD'], '2019-10-03'), :])
print(stocks.loc[(['BIDU', 'JD'], '2019-10-03'), '收盘'])
print(stocks.loc[('BIDU', ['2019-10-02', '2019-10-03']), '收盘'])

# slice(None)代表筛选这一索引的所有内容
print(stocks.loc[(slice(None), ['2019-10-02', '2019-10-03']), :])
print(stocks.reset_index())