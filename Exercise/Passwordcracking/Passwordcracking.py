#!/usr/bin/env python
# encoding: utf-8
'''
@File  : FileZip.py
@Date  : 2021/10/27 23:22
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python实现zip文件夹压缩
'''
import os, sys, zipfile, itertools

filename = "123.zip"

def uncompress(filename, password):
    try:
        with zipfile.ZipFile(filename) as zfile:
            zfile.extractall("./", pwd=password.encode("utf8"))
        return True
    except:
        return False

chars = "abcdefjhijklmnopqrstuvwxyz0123456789"
for c in itertools.permutations(chars, 4):
    password = "".join(c)
    print(password)
    result = uncompress(filename, password)
    if not result:
        print("解压失败", password)
    else:
        print("解压成功", password)
        break