#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 004_print_primes.py
@Date  : 2021/11/1 23:11
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

# 需要优化算法
def is_prime(number):
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True

def print_prime(begin, end):
    for number in range(begin, end+1):
        if is_prime(number):
            print(f'{number} is prime')

begin = 0
end = 100
print_prime(begin, end)

