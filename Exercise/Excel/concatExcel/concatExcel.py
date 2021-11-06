#!/usr/bin/env python
# encoding: utf-8
'''
@File  : concatExcel.py
@Date  : 2021/10/26 0:30
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python批量合并多格式相同Excel文件，到一个表中
'''
import pandas as pd
import os

fname_list = []
for fname in os.listdir("."):
    if fname.startswith("产品统计表") and fname.endswith(".xlsx"):
        fname_list.append(pd.read_excel(fname))

fname_all = pd.concat(fname_list)
fname_all.to_excel("产品统计表.xlsx", index=False)