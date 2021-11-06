#!/usr/bin/env python
# encoding: utf-8
'''
@File  : PivotingExcel.py
@Date  : 2021/10/26 22:53
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python办公自动化，读取Excel实现数据透视表
'''
import pandas as pd

df = pd.read_excel("数据透视.xlsx")

# print(df.head())
df_pivot = pd.pivot_table(df,
                          index=["日期", "公司"],
                          columns="数据项",
                          values="数据值"
                          )
# print(df_pivot)
df_pivot.to_excel("结果表.xlsx")