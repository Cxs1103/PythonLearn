#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 17_pandas_map_applymap.py
@Date  : 2021/11/29 20:54
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :

Pandas的数据转换函数map、apply、applymap
数据转换函数对比：map、apply、applymap：

map：只用于Series，实现每个值->值的映射；
apply：用于Series实现每个值的处理，用于Dataframe实现某个轴的Series的处理；
applymap：只能用于DataFrame，用于处理该DataFrame的每个元素；
'''

# 1. map用于Series值的转换
# 实例：将股票代码英文转换成中文名字
# Series.map(dict) or Series.map(function)均可
import pandas as pd

stocks = pd.read_excel('./datas/互联网公司股票.xlsx')
print(stocks.head())

print(stocks['公司'].unique())

# 公司股票代码到中文的映射，注意这里是小写
dict_company_names = {
    "bidu": "百度",
    "baba": "阿里巴巴",
    "iq": "爱奇艺",
    "jd": "京东"
}

# 方法1：Series.map(dict)
stocks['公司中文1'] = stocks['公司'].str.lower().map(dict_company_names)
print(stocks.head())

# 方法2：Series.map(function)
# function的参数是Series的每个元素的值
stocks['公司中文2'] = stocks['公司'].map(lambda x: dict_company_names[x.lower()])
print(stocks.head())

"""
2. apply用于Series和DataFrame的转换
Series.apply(function), 函数的参数是每个值
DataFrame.apply(function), 函数的参数是Series
"""
# Series.apply(function)
# function的参数是Series的每个值
stocks['公司中文3'] = stocks['公司'].apply(
    lambda x: dict_company_names[x.lower()]
)
print(stocks.head())

# DataFrame.apply(function)
# function的参数是对应轴的Series
stocks["公司中文4"] = stocks.apply(
    lambda x: dict_company_names[x['公司'].lower()],
    axis=1
)
print(stocks.head())
"""
注意这个代码：
1、apply是在stocks这个DataFrame上调用；
2、lambda x的x是一个Series，因为指定了axis=1所以Seires的key是列名，可以用x['公司']获取
"""
# 3. applymap用于DataFrame所有值的转换
sub_df = stocks[['收盘', '开盘', '高', '低', '交易量']]
print(sub_df.head())

# 将这些数字取整数，应用于所有元素
print(sub_df.applymap(lambda x: int(x)))

stocks.loc[:, ['收盘', '开盘', '高', '低', '交易量']] = sub_df.applymap(lambda x: int(x))
print(stocks.head())
