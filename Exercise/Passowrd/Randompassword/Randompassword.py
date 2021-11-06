#!/usr/bin/env python
# encoding: utf-8
'''
@File  : Randompassword.py
@Date  : 2021/10/27 21:45
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : python随机密码生成器
'''
import string,random
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

chars = list(string.ascii_letters + string.digits + string.punctuation)
random.shuffle(chars)
print("".join(chars[:15]))