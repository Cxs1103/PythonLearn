#!/usr/bin/env python
# encoding: utf-8
'''
@File  : contrastExcel.py
@Date  : 2021/10/26 1:08
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : python对比两份excel表格的差异性
'''
import xlwings as xw

app = xw.App(visible=False, add_book=False)
book = app.books.open("产品统计表-背包.xlsx")
book_back = app.books.open("产品统计表-背包 - 副本.xlsx")

for row in book.sheets[0].range("A1").expand():
    for cell in row:
        back_cell = book_back.sheets[0].range(cell.address)
        if cell.value != back_cell.value:
            cell.color = back_cell.color = (255, 0, 0)

book.save()
book.close()
book_back.save()
book_back.close()
app.quit()