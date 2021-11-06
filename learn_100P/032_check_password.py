#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 032_check_password.py
@Date  : 2021/11/6 1:40
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import re


def check_password(password):
    if not 10 <= len(password) <= 20:
        return False, "密码需要在10-20位之间"
    if not re.findall(r"[a-z]", password):
        return False, "必须包含至少一个小写字母"
    if not re.findall(r"[A-Z]", password):
        return False, "必须包含至少一个大写字母"
    if not re.findall(r"[0-9]", password):
        return False, "必须包含至少一个数字"
    if not re.findall(r"[^a-zA-Z0-9]", password):
        return False, "必须包含至少一个特殊字符"
    return True, None


print("HelloWorld@1313", check_password("HelloWorld@1313"))
print("HelloWorld1313", check_password("HelloWorld1313"))
print("HelloWorld1jjjj", check_password("HelloWorld1jjjj"))
print("HelloWorld@jjjj", check_password("HelloWorld@jjjj"))
print("helloworld@1111", check_password("helloworld@1111"))
