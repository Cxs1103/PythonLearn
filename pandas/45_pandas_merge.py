#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 45_pandas_merge.py
@Date  : 2021/12/12 14:42
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas实现模糊匹配Merge数据的方法
'''

import pandas as pd
import numpy as np
import re

# 1. 两份数据

# 关键词数据
df_keyword = pd.DataFrame({
    "keyid": np.arange(5),
    "keyword": ["numpy", "pandas", "matplotlib", "sklearn", "tensorflow"]
})
print(df_keyword)

# 句子数据
df_sentence = pd.DataFrame({
    "senid": np.arange(10, 17),
    "sentence": [
        "怎样用Pandas实现数据的Merge？",
        "Python之Numpy详细教程",
        "怎样使用Pandas批量拆分与合并Excel文件？",
        "怎样使用Pandas的map和apply函数？",
        "深度学习及TensorFlow简介",
        "Tensorflow和Numpy的关系",
        "基于sklearn的一些机器学习的代码"
    ]
})
print(df_sentence)

# 方法1：暴力笛卡尔积 + 过滤
# 新增数字完全一样的列
df_keyword["match"] = 1
df_sentence["match"] = 1

print(df_keyword)
print(df_sentence)

# 实现merge
# 结果行数 = A表行数 * B表行数
df_merge = pd.merge(df_keyword, df_sentence)
print(df_merge)


# 过滤出结果
def match_func(row):
    return re.search(row["keyword"], row["sentence"], re.IGNORECASE) is not None


print(df_merge[df_merge.apply(match_func, axis=1)])

# 方法2：小表变字典做merge最后explode
# 构建要join的key:index的关系
key_word_dict = {
    row.keyword: row.keyid
    for row in df_keyword.itertuples()
}
print(key_word_dict)


# 大表搜寻小表字典
def merge_func(row):
    # 新增一列，表示能匹配的keyids
    row["keyids"] = [
        keyid
        for key_word, keyid in key_word_dict.items()
        if re.search(key_word, row["sentence"], re.IGNORECASE)
    ]
    return row


df_merge = df_sentence.apply(merge_func, axis=1)

print(df_merge)

# 展开然后做merge
print(df_merge.explode("keyids"))

df_result = pd.merge(
    left=df_merge.explode("keyids"),
    right=df_keyword,
    left_on="keyids",
    right_on="keyid"
)
print(df_result)