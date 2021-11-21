#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 06_clean_null_values.py
@Date  : 2021/11/21 16:38
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas对缺失值的处理
Pandas使用这些函数处理缺失值：
    isnull和notnull：检测是否是空值，可用于df和series
    dropna：丢弃、删除缺失值
        axis : 删除行还是列，{0 or ‘index’, 1 or ‘columns’}, default 0
        how : 如果等于any则任何值为空都删除，如果等于all则所有值都为空才删除
        inplace : 如果为True则修改当前df，否则返回新的df
    fillna：填充空值
        value：用于填充的值，可以是单个值，或者字典（key是列名，value是值）
        method : 等于ffill使用前一个不为空的值填充forword fill；等于bfill使用后一个不为空的值填充backword fill
        axis : 按行还是列填充，{0 or ‘index’, 1 or ‘columns’}
        inplace : 如果为True则修改当前df，否则返回新的df
'''
import pandas as pd

fpath = "./datas/student_excel.xlsx"

df = pd.read_excel(fpath, skiprows=2)
print(df)

# 是否有空值
print(df.isnull())

# 单独列
print(df["分数"].isnull())

# 筛选没有空分数的所有行
print(df.loc[df['分数'].notnull(), :])

# 删除掉全是空值的列
df.dropna(axis="columns", how='all', inplace=True)
print(df)

# 删除掉全是空值的行
df.dropna(axis="index", how='all', inplace=True)
print(df)

# 将分数列为空的填充为0分
print(df.fillna({"分数":0}))
df.loc[:, "分数"] = df["分数"].fillna(0)
print(df)

# 将姓名的缺失值填充
# 使用前面的有效值填充，用ffill：forward fill
df.loc[:, '姓名'] = df['姓名'].fillna(method="ffill")
print(df)

# 输出处理好的数据到excel中,index=Flase表示，删除默认生成的序列
df.to_excel('./datas/student_excel_clean.xlsx', index=False)