#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 23_pandas_vlookup.py
@Date  : 2021/12/2 22:03
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎样实现Excel的vlookup并且在指定列后面输出？
背景：

有两个excel，他们有相同的一个列；
按照这个列合并成一个大的excel，即vlookup功能，要求：
只需要第二个excel的少量的列，比如从40个列中挑选2个列
新增的来自第二个excel的列需要放到第一个excel指定的列后面；
将结果输出到一个新的excel;
'''
import pandas as pd

# 步骤1：读取两个数据表
df_sinfo = pd.read_excel('./datas/vlookup/学生信息表.xlsx')
df_grade = pd.read_excel('./datas/vlookup/学生成绩表.xlsx')
print(df_grade.head())
print(df_sinfo.head())

# 目标：怎样将第二个“学生信息表”的姓名、性别两列，添加到第一个表“学生成绩表”，
# 并且放在第一个表的“学号”列后面？

# 步骤2：实现两个表的关联
# 即excel的vloopup功能
# 只筛选第二个表的少量的列
df_sinfo = df_sinfo[['学号', '姓名', '性别']]
print(df_sinfo.head())

df_merge = pd.merge(left=df_grade, right=df_sinfo, left_on='学号', right_on='学号')
print(df_merge.head())

# 步骤3：调整列的顺序
print(df_merge.columns)

# 问题：怎样将'姓名', '性别'两列，放到'学号'的后面？
# 接下来需要用Python的语法实现列表的处理
print(pd.__version__)

# 将columns变成python的列表形式
new_colmuns = df_merge.columns.to_list()
print(new_colmuns)

# 按逆序insert，会将"姓名"，"性别"放到"学号"的后面
for name in ['姓名', '性别'][::-1]:
    new_colmuns.remove(name)
    new_colmuns.insert(new_colmuns.index('学号') + 1, name)
print(new_colmuns)

df_merge = df_merge.reindex(columns=new_colmuns)
print(df_merge.head())

# 步骤4：输出最终的Excel文件
df_merge.to_excel('./datas/vlookup/合并之后的表格.xlsx', index=False)
