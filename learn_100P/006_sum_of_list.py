#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 006_sum_of_list.py
@Date  : 2021/11/2 23:04
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total += item
    return total

list1 = [2, 3, 4, 7]
list2 = [26, 35, 34, 27]

print(f'list1 sum is :' , sum_of_list(list1))
print(f'list2 sum is :' , sum_of_list(list2))

print(f'list2 sum is :' , sum(list1))
print(f'list2 sum is :' , sum(list2))