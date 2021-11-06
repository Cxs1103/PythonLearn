#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 005_sum_of_square.py
@Date  : 2021/11/2 22:59
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import math

def sum_of_square(n):
    result = 0
    for number in range(1, n+1):
        result += number*number
    return result

print(f'3 sum of square is :', sum_of_square(3))
print(f'5 sum of square is :', sum_of_square(5))
print(f'10 sum of square is :', sum_of_square(10))