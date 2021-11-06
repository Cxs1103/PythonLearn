#!/usr/bin/env python
# encoding: utf-8
'''
@File  : autoUploadimage.py
@Date  : 2021/10/23 11:24
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import flask
from flask import request
import os

app = flask.Flask(__name__)

# 图片存储服务
@app.route("/upload_images/", methods=["GET", "POST"])
def upload_images():
    if request.method == "POST":
        file = request.files["file"]
        file_name = "./static/" + file.filename
        print("收到文件：", file_name)
        file.save(file_name)
        return "Success"
    else :
        return "Success get"


# 图片展示
@app.route("/query_images", methods=["GET"])
def query_images():
    dir_name = "static"
    html = "<html><body><ul>"
    fnames = sorted([fname for fname in os.listdir(dir_name)
                if fname.endswith(".png")], reverse=True)
    for fname in fnames[:3]:
        html += f"""
            {fname}: <br/>
            <img width='80%' src='{dir_name}/{fname}' />
            <br /><br />
        """
    html += "</ul></body></html>"
    return html

app.run("0.0.0.0", 8888)