#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 09_string_structure.py
@Date  : 2021/11/21 18:48
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas字符串处理
前面我们已经使用了字符串的处理函数：
df["bWendu"].str.replace("℃", "").astype('int32')

Pandas的字符串处理：

使用方法：先获取Series的str属性，然后在属性上调用函数；
只能在字符串列上使用，不能数字列上使用；
Dataframe上没有str属性和处理方法
Series.str并不是Python原生字符串，而是自己的一套方法，不过大部分和原生str很相似；
Series.str字符串方法列表参考文档:
https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handling

本节演示内容：

获取Series的str属性，然后使用各种字符串处理函数
使用str的startswith、contains等bool类Series可以做条件查询
需要多次str处理的链式操作
使用正则表达式的处理
'''
import pandas as pd

# 读取北京2018年天气数据
fpath = "./datas/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)

print(df)
print(df.dtypes)

# 获取Series的str属性，使用各种字符串处理函数
print(df["bWendu"].str)
print(df['bWendu'].str.replace("℃", ""))

# 判断是不是数字
print(df['bWendu'].str.isnumeric())

# 字符串长度
print(df['fengxiang'].str.len())

# 使用str的startswith、contains等得到bool的Series可以做条件查询
condition = df["ymd"].str.startswith("2018-03")
print(condition)
print(df[condition].head())

"""
需要多次str处理的链式操作
怎样提取201803这样的数字月份？
1、先将日期2018-03-31替换成20180331的形式
2、提取月份字符串201803
"""
print(df['ymd'].str.replace("-", ""))

# 每次调用函数，都返回一个新Series(所以会报错)
# print(df["ymd"].str.replace("-", "").slice(0, 6))

# 需要重新调用str函数
print(df["ymd"].str.replace("-", "").str.slice(0, 6))

print("=================================================")

# slice就是切片语法，可以直接用
print(df["ymd"].str.replace("-", "").str[0:6])

# 使用正则表达式的处理
def get_YearMonthDay(x):
    year, month, day = x['ymd'].split("-")
    return f"{year}年{month}月{day}日"
df["中文日期"] = df.apply(get_YearMonthDay, axis=1)

print(df["中文日期"])

# 问题：怎样将“2018年12月31日”中的年、月、日三个中文字符去除
# 方法1：链式replace
print(df["中文日期"].str.replace("年", "").str.replace("月","").str.replace("日", ""))

print("=================================================")

#Series.str默认就开启了正则表达式模式
# 方法2：正则表达式替换
print(df["中文日期"].str.replace("[年月日]", ""))