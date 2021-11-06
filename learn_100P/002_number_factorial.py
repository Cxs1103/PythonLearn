#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 002_number_factorial.py
@Date  : 2021/11/1 22:30
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

print(f'6 的阶乘是：', factorial(6))
print(f'10 的阶乘是：', factorial(10))