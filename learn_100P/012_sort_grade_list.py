#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 012_sort_grade_list.py
@Date  : 2021/11/3 22:52
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''


def read_file():
    read_result = []
    with open('./datas/012_grade_file.txt') as fin:
        for line in fin:
            line = line[:-1]
            read_result.append(line.split(","))
    return read_result


# 读取文件
datas = read_file()
print(datas)


# 排序文件
def sort_grades(datas):
    sort_result = sorted(datas, key=lambda x: int(x[2]), reverse=True)
    return sort_result


datas = sort_grades(datas)
print(datas)


# 写出文件
def write_file(datas):
    with open('./datas/012_grade_file_output.txt', 'w') as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")


datas = write_file(datas)
print(datas)
