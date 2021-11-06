#!/usr/bin/env python
# encoding: utf-8
'''
@File  : passwordmanager.py
@Date  : 2021/10/27 22:12
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python实现自己的密码管理器
'''
import sys
import os
import json
import string, random

password_file = "my_password.txt"

def get_password_dict():
    if os.path.isfile(password_file):
        with open(password_file) as fin:
            return json.loads(fin.read())
    else:
        return {}

def show_password():
    password_dict = get_password_dict()
    for key, value in password_dict.items():
        print(f"网站：{key} , 密码：{value}" )

def get_new_password(pwd_len=15):
    chars = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(chars)
    return "".join(chars[:pwd_len])


def add_password(website):
    password_dict = get_password_dict()
    password_dict[website] = get_new_password()
    with open(password_file, "w") as fout:
        fout.write(json.dumps(password_dict))

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "show":
        show_password()

    if len(sys.argv) == 3 and sys.argv[1] == "add":
        add_password(sys.argv[2])