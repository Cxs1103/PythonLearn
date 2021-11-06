#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 007_print_even_numbers.py
@Date  : 2021/11/2 23:15
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

def print_even_number(begin, end):
    list_number = []
    for number in range(begin, end):
        if number % 2 == 0:
            list_number.append(number)
    return list_number

print(f'1 to 15 even number is :', print_even_number(1, 15))
print(f'15 to 100 even number is :', print_even_number(15, 100))

data = [item for item in range(1,15) if item %2==0]
print(f'1 to 15 even number is :', data)