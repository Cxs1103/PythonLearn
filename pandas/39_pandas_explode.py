#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 39_pandas_explode.py
@Date  : 2021/12/11 13:22
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas处理Excel - 复杂多列到多行转换
用户需求图片
https://github.com/peiss/ant-learn-pandas/raw/affe42ca8f767bd2d9d8fb75748b1f7e62a56993//course_datas/c39_explode_to_manyrows/%E7%94%A8%E6%88%B7%E9%9C%80%E6%B1%82%E5%9B%BE%E7%89%87.png

分析：
一行变多行，可以用explode实现；
要使用explode，需要先将多列变成一列；
注意有的列为空，需要做空值过滤；

'''
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
# 1. 读取数据
file_path = "./datas/explode_to_manyrows/读者提供的数据-输入.xlsx"

df = pd.read_excel(file_path)
print(df.head())

# 2. 把多列合并到一列
# 提取待合并的所有列名，一会可以把它们drop掉
merge_names = list(df.loc[:, "Supplier":].columns.values)  # ‘  "Supplier":  ’匹配所有包含这个的列
# print(df.loc[:,"Supplier":])
print(merge_names)


def merge_cols(x):
    """
    x是一个行Series，把它们按分隔符合并
    """
    # 删除为空的列
    x = x[x.notna()]

    # 使用x.values用于合并
    y = x.values

    # 合并后的列表，每个元素是"Supplier" + "Supplier PN"对
    result = []

    # range的步长为2，目的是每两列做合并
    for idx in range(0, len(y), 2):
        # 使用竖线作为"Supplier" + "Supplier PN"之间的分隔符
        result.append(f"{y[idx]} | {y[idx + 1]}")
    # 将所有两两对，用#分割，返回一个大字符串
    return "#".join(result)


# 添加新列，把待合并的所有列变成一个大字符串
df["merge"] = df.loc[:, "Supplier":].apply(merge_cols, axis=1)
print(df)

# 把不用的列删除掉
df.drop(merge_names, axis=1, inplace=True)
print(df)

# 3. 使用explode把一列变多行
df["merge"] = df["merge"].str.split("#")
print(df)

# 执行explode变成多行
df_explode = df.explode("merge")
print(df_explode)

# 4. 将一列还原成结果的多列
# 分别从merge中提取两列
df_explode["Supplier"] = df_explode["merge"].str.split("|").str[0]
df_explode["Supplier PN"] = df_explode["merge"].str.split("|").str[1]
print(df_explode)

# 把merge列删除掉，得到最终数据
df_explode.drop("merge", axis=1, inplace=True)
print(df_explode)

# 5. 输出到结果Excel
df_explode.to_excel("./datas/explode_to_manyrows/读者提供的数据-输出.xlsx")