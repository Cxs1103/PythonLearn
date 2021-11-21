#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 03_query_datas.py
@Date  : 2021/11/21 11:42
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas查询数据的几种方法:
df.loc方法，根据行、列的标签值查询
df.iloc方法，根据行、列的数字位置查询
df.where方法
df.query方法
.loc既能查询，又能覆盖写入，强烈推荐！

Pandas使用df.loc查询数据的方法:
使用单个label值查询数据
使用值列表批量查询
使用数值区间进行范围查询
使用条件表达式查询
调用函数查询

注意
以上查询方法，既适用于行，也适用于列
注意观察降维dataFrame>Series>值
'''
import pandas as pd

print(pd.__version__)

df = pd.read_csv("./datas/beijing_tianqi_2018.csv")
print(df.head())

# 设定索引为日期，方便按日期筛选
df.set_index('ymd', inplace=True)
print(df.index)
print("==================================================")
print(df.head())

# 替换掉温度的后缀℃
# print(df.loc[:, 'bWendu'])
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
print(df.head())
print(df.dtypes)

print("==================================================")
"""
使用单个label值查询数据
行或者列，都可以只传入单个值，实现精确匹配
"""
# 根据索引，得到单个值
print(df.loc['2018-12-30', 'bWendu'])

print("==================================================")

# 得到一个Series
print(df.loc['2018-01-03', ['bWendu', 'yWendu']])

# 使用值列表批量查询

# 得到Series
print(df.loc[['2018-01-03', '2018-01-04', '2018-01-05'], 'bWendu'])

# 得到dataframe
print(df.loc[['2018-01-03', '2018-01-04', '2018-01-05'], ['bWendu', 'yWendu']])

"""
使用数值区间进行范围查询
注意：区间既包含开始，也包含结束
"""
# 行index按区间
print(df.loc['2018-01-05':'2018-01-08', 'bWendu'])

# 行index按区间
print(df.loc['2018-01-08', 'bWendu':'fengxiang'])

# 行和列都按区间查询
print(df.loc['2018-01-08':'2018-01-11', 'bWendu':'fengxiang'])

"""
使用条件表达式查询
bool列表的长度得等于行数或者列数
"""

# 简单条件查询，最低温度低于-10度的列表
print(df.loc[df['yWendu'] < -10, :])
print(df['yWendu'] < -10)

# 复杂条件查询，查一下我心中的完美天气
# 注意，组合条件用&符号合并，每个条件判断都得带括号
print(df.loc[(df['bWendu'] <= 30) & (df['yWendu'] >= 15) & (df['tianqi'] == '晴') & (df['aqiLevel'] == 1), :])

# 再次观察这里的boolean条件
print((df['bWendu'] <= 30) & (df['yWendu'] >= 15) & (df['tianqi'] == '晴') & (df['aqiLevel'] == 1))

# 调用函数查询
# 直接写lambda表达式
print(df.loc[lambda df: (df['bWendu'] <= 30) & (df['yWendu'] >= 15), :])

# 编写自己的函数，查询9月份，空气质量好的数据
def query_my_data(df):
    return df.index.str.startswith("2018-09") & (df["aqiLevel"] == 1)

print(df.loc[query_my_data, :])
