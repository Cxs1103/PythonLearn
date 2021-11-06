#!/usr/bin/env python
# encoding: utf-8
'''
@File  : FileZip.py
@Date  : 2021/10/27 23:22
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python实现zip文件夹压缩
'''
import os, sys, zipfile

def do_zip_compress(dirname):
    output_name = f"{dirname}.zip"
    zip = zipfile.ZipFile(output_name, "w", zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(dirname):
        for file in files:
            zip.write(os.path.join(root, file))
    zip.close()

if __name__ == "__main__":
    dirname = sys.argv[1]
    if not os.path.isdir(dirname):
        raise Exception(f"这个不是目录：{dirname}")

    do_zip_compress(dirname)