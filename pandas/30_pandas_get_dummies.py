#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 30_pandas_get_dummies.py
@Date  : 2021/12/4 22:08
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :

Pandas的get_dummies用于机器学习的特征处理
分类特征有两种：

普通分类：性别、颜色
顺序分类：评分、级别
对于评分，可以把这个分类直接转换成1、2、3、4、5表示，因为它们之间有顺序、大小关系

但是对于颜色这种分类，直接用1/2/3/4/5/6/7表达，是不合适的，因为机器学习会误以为这些数字之间有大小关系

get_dummies就是用于颜色、性别这种特征的处理，也叫作one-hot-encoding处理

比如：

男性：1 0
女性：0 1
这就叫做one-hot-encoding，是机器学习对类别的特征处理
'''
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
# 显示所有列
# pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)


df_train = pd.read_csv("./datas/titanic/titanic_train.csv")
print(df_train.head())

df_train.drop(columns=["Name", "Ticket", "Cabin"], inplace=True)
print(df_train.head())
print(df_train.info())
"""
特征说明：
数值特征：Fare
分类-有序特征：Age
分类-普通特征：PassengerId、Pclass、Sex、SibSp、Parch、Embarked
Survived为要预测的Label
"""

# 2、分类有序特征可以用数字的方法处理
# 使用年龄的平均值，填充空值
df_train["Age"] = df_train["Age"].fillna(df_train["Age"].mean())
print(df_train)

# 3、普通无序分类特征可以用get_dummies编码
# 其实就是one-hot编码
print(pd.get_dummies(df_train["Sex"]).head())
print(pd.get_dummies(df_train["Sex"]))

# 注意，One-hot-Encoding一般要去掉一列，不然会出现dummy variable trap，
# 因为一个人不是male就是femal，它俩有推导关系 https://www.geeksforgeeks.org/ml-dummy-variable-trap-in-regression-models/

# 便捷方法，用df全部替换
# 便捷方法，用df全部替换
needcode_cat_columns = ["Pclass","Sex","SibSp","Parch","Embarked"]
df_coded = pd.get_dummies(
    df_train,
    # 要转码的列
    columns=needcode_cat_columns,
    # 生成的列名的前缀
    prefix=needcode_cat_columns,
    # 把空值也做编码
    dummy_na=True,
    # 把1 of k移除（dummy variable trap）
    drop_first=True
)
print(df_coded.head())

# 4、机器学习模型训练
y = df_coded.pop("Survived")
print(y.head())

X = df_coded
print(X.head())

from sklearn.linear_model import LogisticRegression
# 创建模型对象
logreg = LogisticRegression(solver='liblinear')

# 实现模型训练
print(logreg.fit(X, y))
print(logreg.score(X, y))
