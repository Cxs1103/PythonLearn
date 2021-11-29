#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 18_pandas_groupbu_apply.py
@Date  : 2021/11/29 22:14
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎样对每个分组应用apply函数?
知识：Pandas的GroupBy遵从split、apply、combine模式
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/pandas-split-apply-combine.png
这里的split指的是pandas的groupby，我们自己实现apply函数，apply返回的结果由pandas进行combine得到结果

GroupBy.apply(function)
function的第一个参数是dataframe
function的返回结果，可是dataframe、series、单个值，甚至和输入dataframe完全没关系
本次实例演示：
怎样对数值列按分组的归一化？
怎样取每个分组的TOPN数据？
实例1：怎样对数值列按分组的归一化？
将不同范围的数值列进行归一化，映射到[0,1]区间：

更容易做数据横向对比，比如价格字段是几百到几千，增幅字段是0到100
机器学习模型学的更快性能更好
归一化的公式：
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/Normalization-Formula.jpg
演示：用户对电影评分的归一化
每个用户的评分不同，有的乐观派评分高，有的悲观派评分低，按用户做归一化
'''

import pandas as pd

ratings = pd.read_csv(
    './datas/movielens_1m/ratings.dat',
    sep="::",
    engine='python',
    names="UserID::MovieID::Rating::Timestamp".split("::")
)
print(ratings.head())


# 实现按照用户ID分组，然后对其中一列归一化
def ratings_norm(df):
    """
    @param df：每个用户分组的dataframe
    """
    min_value = df["Rating"].min()
    max_value = df["Rating"].max()
    df["Rating_norm"] = df["Rating"].apply(
        lambda x: (x - min_value) / (max_value - min_value))
    return df


ratings = ratings.groupby("UserID").apply(ratings_norm)
print(ratings.head())
# 可以看到UserID==1这个用户，Rating==3是他的最低分，是个乐观派，我们归一化到0分；

# 实例2：怎样取每个分组的TOPN数据？
# 获取2018年每个月温度最高的2天数据
fpath = "./datas/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
print(df.head())

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

# 新增一列为月份
df['month'] = df['ymd'].str[:7]
print(df.head())


def getWenduTopN(df, topn):
    """
    这里的df，是每个月份分组group的df
    """
    return df.sort_values(by="bWendu")[['ymd', 'bWendu']][-topn:]


print(df.groupby("month").apply(getWenduTopN, topn=2).head())
# grouby的apply函数返回的dataframe，其实和原来的dataframe其实可以完全不一样