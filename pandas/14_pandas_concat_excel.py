#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 14_pandas_concat_excel.py
@Date  : 2021/11/27 23:28
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas批量拆分Excel与合并Excel
实例演示：

将一个大Excel等份拆成多个Excel
将多个小Excel合并成一个大Excel并标记来源
'''
import pandas as pd
import os

work_dir = "./datas/excel_split-merge"
split_dir = "./datas/excel_split-merge/split"

if not os.path.exists(split_dir):
    os.mkdir(split_dir)

df_source = pd.read_excel(f"{work_dir}/crazyant_blog_articles_source.xlsx")
print(df_source.head())

print(df_source.index)

print(df_source.shape)

total_row_count = df_source.shape[0]
print(total_row_count)

"""
一、将一个大Excel等份拆成多个Excel
使用df.iloc方法，将一个大的dataframe，拆分成多个小dataframe
将使用dataframe.to_excel保存每个小Excel
1、计算拆分后的每个excel的行数
"""
# 任务接受者
user_names = ["xiao_shuai", "xiao_wang", "xiao_ming", "xiao_lei", "xiao_bo", "xiao_hong"]

# 每个人的任务数目
split_size = total_row_count // len(user_names)
if total_row_count % len(user_names) != 0:
    split_size += 1

print(split_size)

# 2、拆分成多个dataframe
df_subs = []
for idx, user_name in enumerate(user_names):
    # iloc的开始索引
    begin = idx * split_size
    # iloc的结束索引
    end = begin + split_size
    # 实现df按照iloc拆分
    df_sub = df_source.iloc[begin:end]
    # 将每个子df存入列表
    df_subs.append((idx, user_name, df_sub))
print(df_subs)

# 3、将每个datafame存入excel
for idx, user_name, df_sub in df_subs:
    file_name = f"{split_dir}/crazyant_blog_articles_{idx}_{user_name}.xlsx"
    df_sub.to_excel(file_name, index=False)

"""
二、合并多个小Excel到一个大Excel
遍历文件夹，得到要合并的Excel文件列表
分别读取到dataframe，给每个df添加一列用于标记来源
使用pd.concat进行df批量合并
将合并后的dataframe输出到excel
1. 遍历文件夹，得到要合并的Excel名称列表
"""
excel_names = []
for excel_name in os.listdir(split_dir):
    excel_names.append(excel_name)

print(excel_names)

# 2. 分别读取到dataframe
df_list = []
for excel_name in excel_names:
    # 读取每个excel到df
    excel_path = f"{split_dir}/{excel_name}"
    df_split = pd.read_excel(excel_path)

    # 得到username
    username = excel_name.replace("crazyant_blog_articles_", "").replace(".xlsx", "")[2:]
    print(excel_name, username)

    # 给每个df添加一列，即用户名
    df_split["username"] = username

    df_list.append(df_split)

# 使用pd.concat进行合并
df_megerd = pd.concat(df_list)
print(df_megerd.shape)
print(df_megerd.head())
print(df_megerd["username"].value_counts())
df_megerd.to_excel(f"{work_dir}/crazyant_blog_articles_merged.xlsx", index=False)
