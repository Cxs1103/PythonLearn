#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 28_pandas_Categorical.py
@Date  : 2021/12/4 17:02
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas的Categorical数据类型可以降低数据存储提升计算速度
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//other_files/pandas-categorical.png
'''
import pandas as pd
import timeit

df = pd.read_csv(
    "./datas/movielens_1m/users.dat",
    sep='::',
    engine='python',
    header=None,
    names="UserID::Gender::Age::Occupation::Zip-code".split("::")
)
print(df.head())
print(df.info)

df.info(memory_usage="deep")

df_cat = df.copy()
print(df_cat.head())

# 2、使用categorical类型降低存储量
df_cat["Gender"] = df_cat["Gender"].astype("category")
print(df_cat.info(memory_usage="deep"))
print(df_cat.head())

print(df_cat["Gender"].value_counts())

# 3、提升运算速度
# 计时，查询Gender的size(大小)数据性能,number=1000
print(timeit.timeit(stmt='df.groupby("Gender").size()',
                    setup='import pandas as pd;'
                          'df = pd.read_csv("./datas/movielens_1m/users.dat",sep="::",engine="python",header=None,names="UserID::Gender::Age::Occupation::Zip-code".split("::"))',
                    number=1000))

# 对比category类型
print(timeit.timeit(stmt='df_cat.groupby("Gender").size()',
                    setup='import pandas as pd;'
                          'df = pd.read_csv("./datas/movielens_1m/users.dat",sep="::",engine="python",header=None,names="UserID::Gender::Age::Occupation::Zip-code".split("::"));'
                          'df_cat = df.copy();'
                          'df_cat["Gender"] = df_cat["Gender"].astype("category")',
                    number=1000))
# 本次结果
# Gender类型：dtypes: object 时间为：0.7414556000000001
# Gender类型：dtypes: category 时间为：0.4209611000000002
# 初步计算节约43%的时间