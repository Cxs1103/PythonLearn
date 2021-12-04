#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 27_pandas_data_features.py
@Date  : 2021/12/4 15:35
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎样找出最影响结果的那些特征？
应用场景：

机器学习的特征选择，去除无用的特征，可以提升模型效果、降低训练时间等等
数据分析领域，找出收入波动的最大因素！！
实例演示：泰坦尼克沉船事件中，最影响生死的因素有哪些？
'''

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# 特征最影响结果的K个特征
from sklearn.feature_selection import SelectKBest

# 卡方检验，作为SelectKBest的参数
from sklearn.feature_selection import chi2

# 2、导入泰坦尼克号的数据
df = pd.read_csv("./datas/titanic/titanic_train.csv")
print(df.head())

df = df[["PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]].copy()

print(df.head())

# 3、数据清理和转换
# 3.1 查看是否有空值列
print(df.info())

# 3.2 给Age列填充平均值
df["Age"] = df["Age"].fillna(df["Age"].median())
print(df.head())

# 3.2 将性别列变成数字
# 性别
print(df.Sex.unique())

df.loc[df["Sex"] == "male", "Sex"] = 0
df.loc[df["Sex"] == "female", "Sex"] = 1

print(df.head())

# 3.3 给Embarked列填充空值，字符串转换成数字
# Embarked
print(df.Embarked.unique())

# 填充空值
df["Embarked"] = df["Embarked"].fillna(0)

# 字符串变成数字
df.loc[df["Embarked"] == "S", "Embarked"] = 1
df.loc[df["Embarked"] == "C", "Embarked"] = 2
df.loc[df["Embarked"] == "Q", "Embarked"] = 3

print(df.head())

# 4、将特征列和结果列拆分开
y = df.pop("Survived")
X = df

print(X.head())
print(y.head())

# 5、使用卡方检验选择topK的特征
# 选择所有的特征，目的是看到特征重要性排序
bestfeatures = SelectKBest(score_func=chi2, k=len(X.columns))
fit = bestfeatures.fit(X, y)

# 6、按照重要性顺序打印特征列表
df_scores = pd.DataFrame(fit.scores_)
print(df_scores)

df_columns = pd.DataFrame(X.columns)
print(df_columns)

# 合并两个df
df_feature_scores = pd.concat([df_columns,df_scores],axis=1)

# 列名
df_feature_scores.columns = ['feature_name','Score']  #naming the dataframe columns

# 查看
print(df_feature_scores)

# 降序
print(df_feature_scores.sort_values(by="Score", ascending=False))