#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 35_pandas_groupby_agg.py
@Date  : 2021/12/6 0:38
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas实现groupby聚合后不同列数据统计
电影评分数据集（UserID，MovieID，Rating，Timestamp）

聚合后单列-单指标统计：每个MovieID的平均评分
df.groupby("MovieID")["Rating"].mean()

聚合后单列-多指标统计：每个MoiveID的最高评分、最低评分、平均评分
df.groupby("MovieID")["Rating"].agg(mean="mean", max="max", min=np.min)
df.groupby("MovieID").agg({"Rating":['mean', 'max', np.min]})

聚合后多列-多指标统计：每个MoiveID的评分人数，最高评分、最低评分、平均评分
df.groupby("MovieID").agg( rating_mean=("Rating", "mean"), user_count=("UserID", lambda x : x.nunique())
df.groupby("MovieID").agg( {"Rating": ['mean', 'min', 'max'], "UserID": lambda x :x.nunique()})
df.groupby("MovieID").apply( lambda x: pd.Series( {"min": x["Rating"].min(), "mean": x["Rating"].mean()}))

记忆：agg(新列名=函数)、agg(新列名=(原列名，函数))、agg({"原列名"：函数/列表})
agg函数的两种形式，等号代表“把结果赋值给新列”，字典/元组代表“对这个列运用这些函数”

官网文档：https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.core.groupby.DataFrameGroupBy.agg.html
'''

import pandas as pd
import numpy as np

df = pd.read_csv(
    "./datas/movielens_1m/ratings.dat",
    sep="::",
    engine="python",
    names="UserID::MovieID::Rating::Timestamp".split("::")
)

print(df.head())

# 聚合后单列-单指标统计
# 每个MovieID的平均评分
result = df.groupby("MovieID")["Rating"].mean()
print(result)

print(type(result))

# 聚合后单列-多指标统计
# 每个MoiveID的最高评分、最低评分、平均评分

# 方法1：agg函数传入多个结果列名=函数名形式
result2 = df.groupby("MovieID")["Rating"].agg(mean="mean", min=np.min, max="max")
print(type(result2))
print(result2)

# 方法2：agg函数传入字典，key是column名，value是函数列表
result3 = df.groupby("MovieID").agg(
    {"Rating": ['mean', 'max', np.min]}
)
print(type(result3))
print(result3)

result3.columns = ['age_mean', 'age_max', 'age_min']
print(result3.head())

# 聚合后多列-多指标统计
# 每个MoiveID的评分人数，最高评分、最低评分、平均评分

# 方法1：agg函数传入字典，key是原列名，value是原列名和函数元组
# 回忆：agg函数的两种形式，等号代表“把结果赋值给新列”，字典/元组代表“对这个列运用这些函数”
result4 = df.groupby("MovieID").agg(
    rating_mean=("Rating", "mean"),
    rating_max=("Rating", "max"),
    rating_min=("Rating", "min"),
    user_count=("UserID", lambda x: x.nunique())
)
print(result4)

# 方法2：agg函数传入字典，key是原列名，value是函数列表
# 统计后是二级索引，需要做索引处理
result5 = df.groupby("MovieID").agg(
    {
        "Rating": ['mean', 'min', 'max'],
        "UserID": lambda x: x.nunique()
    }
)
print(result5)
print(result5["Rating"].head())
result5.columns = ["rating_mean", "rating_min", "rating_max", "user_count"]
print(result5.head())


# 方法3：使用groupby之后apply对每个子df单独统计
def agg_func(x):
    """注意：这个x是子DF"""

    # 这个Series会变成一行，字典KEY是列名
    return pd.Series({
        "rating_mean": x["Rating"].mean(),
        "rating_min": x["Rating"].min(),
        "rating_max": x["Rating"].max(),
        "user_count": x["UserID"].nunique(),
    })


result6 = df.groupby("MovieID").apply(agg_func)
print(result6)
