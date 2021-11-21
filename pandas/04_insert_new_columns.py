#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 04_insert_new_columns.py
@Date  : 2021/11/21 14:55
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎样新增数据列？
在进行数据分析时，经常需要按照一定条件创建新的数据列，然后进行进一步分析。

直接赋值
df.apply方法
df.assign方法
按条件选择分组分别赋值
'''
import pandas as pd

df = pd.read_csv("./datas/beijing_tianqi_2018.csv")
print(df.head())

"""
直接赋值的方法
实例：清理温度列，变成数字类型
"""

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())

# 计算温差
df.loc[:, 'wencha'] = df['bWendu'] - df['yWendu']
print(df.head())

"""
添加一列温度类型：
如果最高温度大于33度就是高温
低于-10度是低温
否则是常温
"""


def get_wendu_type(x):
    if x['bWendu'] > 30:
        return "高温"
    if x['yWendu'] < 10:
        return "低温"
    return "常温"


# 注意需要设置axis=1，这是series的index是columns
df.loc[:, 'wendu_type'] = df.apply(get_wendu_type, axis=1)
print(df.head())

# 查看温度类型的计数
print(df['wendu_type'].value_counts())

"""
df.assign方法
Assign new columns to a DataFrame.
Returns a new object with all original columns in addition to new ones.
"""
# 可以同时添加多个新的列,摄氏度转华氏度
#
# new_df = df.assign(
#     yWendu_huashi=lambda df: df["yWendu"] * 9 / 5 + 32,
#     bWendu_huashi=lambda df: df["bWendu"] * 9 / 5 + 32
# )
# print(new_df)
print(df.assign(
    yWendu_huashi=lambda df: df["yWendu"] * 9 / 5 + 32,
    bWendu_huashi=lambda df: df["bWendu"] * 9 / 5 + 32
))

"""
按条件选择分组分别赋值
按条件先选择数据，然后对这部分数据赋值新列
"""
# 高低温差大于10度，则认为温差大


df['wencha_type'] = ''
df.loc[df['bWendu']-df['yWendu'] >10,'wencha_type'] = "温差大"
df.loc[df['bWendu']-df['yWendu'] <=10,'wencha_type'] = "温差小"

print(df["wencha_type"].value_counts())