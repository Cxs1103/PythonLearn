#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 46_pandas_similar.py
@Date  : 2021/12/12 15:23
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
计算每个学生成绩最相似的10个学生
'''
import pandas as pd

pd.set_option("display.max_column", 1000)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 1000)

df = pd.read_csv('./datas/student_grade/学生成绩.csv')
print(df.head())
print(df.shape)

# 1. 进行学生成绩的笛卡尔积
df["one"] = 1
print(df.head())

df_merge = pd.merge(left=df, right=df, left_on="one", right_on="one")
print(df_merge.head(3))
print(df_merge.shape)

# 2. 两两计算相似度
columnes = list(df.columns)
columnes.remove("姓名")
columnes.remove("one")
print(columnes)


def sim_func(row):
    sim_value = 0.0
    for column in columnes:
        sim_value += abs(int(row[column + '_x']) - int(row[column + '_y']))

    return sim_value


df_merge["sim"] = df_merge.apply(sim_func, axis=1)
print(df_merge.head())

df_merge = df_merge[df_merge["姓名_x"] != df_merge["姓名_y"]].copy()
print(df_merge.head())


# 3. 计算每个学生的TOP N的学生
def get_top_student(df_sub):
    df_sort = df_sub.sort_values(by="sim", ascending=False).head(10)
    names = ",".join(list(df_sort["姓名_y"]))
    sims = ",".join([str(x) for x in list(df_sort["sim"])])
    return pd.Series({"names": names, "sims": sims})


df_result = df_merge.groupby("姓名_x").apply(get_top_student)
df_result.to_excel("./datas/student_grade/相似计算结果.xlsx", index=True)
