#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 25_pandas_sklearn.py
@Date  : 2021/12/3 21:28
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas结合Sklearn实现泰坦尼克存活率预测
实例目标：实现泰坦尼克存活预测
处理步骤：
1、输入数据：使用Pandas读取训练数据(历史数据，特点是已经知道了这个人最后有没有活下来)
2、训练模型：使用Sklearn训练模型
3、使用模型：对于一个新的不知道存活的人，预估他存活的概率
'''
# 步骤1：读取训练数据
import pandas as pd

df_train = pd.read_csv('./datas/titanic/titanic_train.csv')
print(df_train.head())

# 其中，Survived==1代表这个人活下来了、==0代表没活下来；其他的都是这个人的信息和当时的仓位、票务情况
# 我们只挑选两列，作为预测需要的特征
feature_cols = ['Pclass', 'Parch']
X = df_train.loc[:, feature_cols]
print(X.head())

# 单独提取是否存活的列，作为预测的目标
y = df_train.Survived
print(y.head())

# 步骤2：训练模型.
from sklearn.linear_model import LogisticRegression
# 创建模型对象
logreg = LogisticRegression()

# 实现模型训练
print(logreg.fit(X, y))
print(logreg.score(X, y))


# 步骤3：对于未知数据使用模型
# 机器学习的核心目标，是使用模型预测未知的事物
# 比如预测股票明天是涨还是跌、一套新的二手房成交价大概多少钱、用户打开APP最可能看那些视频等问题

# 找一个历史数据中不存在的数据
print(X.drop_duplicates().sort_values(by=["Pclass", "Parch"]))

# 预测这个数据存活的概率
print(logreg.predict([[2, 4]]))
print(logreg.predict_proba([[2, 4]]))