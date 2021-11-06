#!/usr/bin/env python
# encoding: utf-8
'''
@File  : default_blueprint.py
@Date  : 2021/10/28 23:22
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 创建一个Blueprint 存储视图
'''

from flask import Blueprint, render_template, request

from English_translate.english_dict import english_dict

dft_blueprint = Blueprint("default", __name__)

@dft_blueprint.route("/index")
def index():
    return "success!!"

@dft_blueprint.route("/main", methods=["post", "get"])
def main():
    result = ""
    if request.method == "POST":
        keyword = request.form.get("keyword")
        print(keyword)
        result = english_dict.query(keyword)
    return render_template("main.html", result=result)