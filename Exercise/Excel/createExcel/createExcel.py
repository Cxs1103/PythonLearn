#!/usr/bin/env python
# encoding: utf-8
'''
@File  : createExcel.py
@Date  : 2021/10/25 0:07
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python按模板新建Excel文件
'''
import shutil
import xlwings as xw

datas = [
    ('销售部', '张三'),
    ('技术部', '李四'),
    ('运营部', '王五'),
    ('财务部', '赵六')
]

app = xw.App(visible=False, add_book=False)

for dept, manager in datas:
    target_excle = f"部门业绩-{dept}.xlsx"
    shutil.copy("部门业绩-模板.xlsx", target_excle)
    workbook = app.books.open(target_excle)
    worksheet = workbook.sheets[0]
    worksheet['A1'].value = worksheet['A1'].value.replace("{dept}", dept)
    worksheet['A2'].value = worksheet['A2'].value.replace("{manager}", manager)
    workbook.save()
    workbook.close()

app.quit()