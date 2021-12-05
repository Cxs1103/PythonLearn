#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 34_pandas_sql.py
@Date  : 2021/12/5 22:43
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas和数据库查询语言SQL的对比
Pandas：Python最流行的数据处理与数据分析的类库
SQL：结构化查询语言，用于对MySQL、Oracle等关系型数据库的增删改查
两者都是对“表格型”数据的操作和查询，所以很多语法都能对应起来

对比列表：

SELECT数据查询
WHERE按条件查询
in和not in的条件查询
groupby分组统计
JOIN数据关联
UNION数据合并
Order Limit先排序后分页
取每个分组group的top n
UPDATE数据更新
DELETE删除数据s
'''
import pandas as pd
import numpy as np

# 显示更多列，最大列数设置为1000列
pd.set_option('display.max_columns', 1000)
# 显示宽度
pd.set_option('display.width', 1000)
# 改变列宽，默认50字符，最大列字符数设置为1000字符
pd.set_option('display.max_colwidth', 1000)

df = pd.read_csv("./datas/titanic/titanic_train.csv")
print(df.head())

# 1. SELECT数据查询
# SQL
sql = """
    SELECT PassengerId, Sex, Age, Survived
    FROM titanic
    LIMIT 5;
"""
# Pandas
print(df[["PassengerId", "Sex", "Age", "Survived"]].head(5))
# df.head(5)类似select * from table limit 5，查询所有的字段

# 2. WHERE按条件查询
# SQL：
sql = """
    SELECT *
    FROM titanic
    where Sex='male' and Age>=20.0 and Age<=40.0
    LIMIT 5;
"""
# Pandas
# 使用括号的方式，级联多个条件|
condition = (df["Sex"] == "male") & (df["Age"] >= 20.0) & (df["Age"] <= 40.0)
print(condition.value_counts())
print(df[condition].head(5))

# 3. in和not in的条件查询
print(df["Pclass"].unique())

# SQL：
sql = """
    SELECT *
    FROM titanic
    where Pclass in (1,2)
    LIMIT 5;
"""

# in
print(df["Pclass"].isin((1, 2)))
print(df[df["Pclass"].isin((1, 2))].head())

# not in
print(df[~df["Pclass"].isin((1, 2))].head())

# 4. groupby分组统计
# 4.1 单个列的聚合
# SQL：
sql = """
    SELECT 
        -- 分性别的存活人数
        sum(Survived),
        -- 分性别的平均年龄
        mean(Age)
        -- 分性别的平均票价
        mean(Fare)
    FROM titanic
    group by Sex
"""

# Pandas
print(df.groupby("Sex").agg({"Survived": np.sum, "Age": np.mean, "Fare": np.mean}))
# 4.2 多个列的聚合
# SQL：
sql = """
    SELECT 
        -- 不同存活和性别分组的，平均年龄
        mean(Age)
        -- 不同存活和性别分组的，平均票价
        mean(Fare)
    FROM titanic
    group by Survived, Sex
"""

# Pandas
print(df.groupby(["Survived", "Sex"]).agg({"Age": np.mean, "Fare": np.mean}))

# 5. JOIN数据关联
# 电影评分数据集，评分表
df_rating = pd.read_csv("./datas/ml-latest-small/ratings.csv")
print(df_rating.head(5))

# 电影评分数据集，电影信息表
df_movies = pd.read_csv("./datas/ml-latest-small/movies.csv")
print(df_movies.head(5))

# SQL：
sql = """
    SELECT *
    FROM 
        rating join movies 
        on(rating.movieId=movies.movieId)
    limit 5
"""

# Pandas
df_merged = pd.merge(left=df_rating, right=df_movies, on="movieId")
print(df_merged.head())

# 6. UNION数据合并
df1 = pd.DataFrame({'city': ['Chicago', 'San Francisco', 'New York City'],
                    'rank': range(1, 4)})
print(df1)

df2 = pd.DataFrame({'city': ['Chicago', 'Boston', 'Los Angeles'],
                    'rank': [1, 4, 5]})
print(df2)

# SQL：
sql = """
    SELECT city, rank
    FROM df1

    UNION ALL

    SELECT city, rank
    FROM df2;
"""

# pandas
print(pd.concat([df1, df2]))

# 7. Order Limit先排序后分页
# SQL：
sql = """
    SELECT *
    from titanic
    order by Fare
    limit 5
"""

print(df.sort_values("Fare", ascending=False).head())

# 8. 取每个分组group的top n
# MYSQL不支持
# Oracle有ROW_NUMBER语法

# 按（Survived，Sex）分组，取Age的TOP 2
print(df.groupby(["Survived", "Sex"]).apply(lambda df: df.sort_values("Age", ascending=False).head(2)))

# 9. UPDATE数据更新
print(df.info())

# SQL：
sql = """
    UPDATE titanic
    set Age=0
    where Age is null
"""

# Pandas
condition = df["Age"].isna()
print(condition.value_counts())

df[condition] = 0
print(df["Age"].isna().value_counts())

# 10. DELETE删除数据
# SQL：
sql = """
    DELETE FROM titanic
    where Age=0
"""
df_new = df[df["Age"] != 0]
print(df_new[df_new["Age"] == 0])
