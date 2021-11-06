#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 009_get_unique_list.py
@Date  : 2021/11/3 22:13
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

lista = [10, 20, 30, 40, 10, 30, 50]


def get_unique_list(lista):
    listb = []
    for item in lista:
        if item not in listb:
            listb.append(item)
    return listb


print(f'source list {lista}, unique list:', get_unique_list(lista))
print(f'source list {lista}, unique list:', list(set(lista)))
