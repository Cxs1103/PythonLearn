#!/usr/bin/env python
# encoding: utf-8
'''
@File  : batchToExcle.py
@Date  : 2021/10/24 23:54
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python批量新建excel文件
'''

import xlwings as xw

app = xw.App(visible=True, add_book=False)

for dept in ["技术部", "销售部", "运营部", "财务部"]:
    workbook = app.books.add()
    workbook.save(f"./部门业绩-{dept}.xlsx")