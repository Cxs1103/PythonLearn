#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 008_remove_number.py
@Date  : 2021/11/2 23:24
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

def remove_number(lista,listb):
    for item in lista:
        listb.remove(item)
    return listb

lista = [3,5,9]
listb = [3,5,7,8,9,10]

print(f'remove {lista} in {listb} result is :', remove_number(lista,listb))

data = [item for item in listb if item not in lista]
print(f'remove {lista} in {listb} result is :', data)
