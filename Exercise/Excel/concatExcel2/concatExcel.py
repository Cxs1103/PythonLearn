#!/usr/bin/env python
# encoding: utf-8
'''
@File  : concatExcel.py.py
@Date  : 2021/10/26 23:13
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python读取多个Excel文件实现汇总统计
'''
import pandas as pd
import os

# 合并数据
direcory = "销售表"
df_list = []
for file in os.listdir(direcory):
    if file.endswith(".xlsx"):
        df_list.append(pd.read_excel(f"{direcory}/{file}"))
df_all = pd.concat(df_list)
# print(df_all)

def compute_data(df_sub):
    return pd.Series({
        "总和": round(df_sub["利润(元)"].sum(), 2),
        "最小": round(df_sub["利润(元)"].min(), 2),
        "最大": round(df_sub["利润(元)"].max(), 2),
        "平均": round(df_sub["利润(元)"].mean(), 2)
    })
df_group = df_all.groupby("产品名称").apply(compute_data)
# print(df_group)

df_group.to_excel("汇总统计.xlsx")