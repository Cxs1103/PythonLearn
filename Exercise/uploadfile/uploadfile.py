#!/usr/bin/env python
# encoding: utf-8
'''
@File  : uploadfile.py
@Date  : 2021/10/23 14:56
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python实现手机给电脑传文件
'''

from flask import Flask,request

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        print("收到文件：", file.filename)
        file.save(f"./datas/upload/{file.filename}")
        return "上传成功"
    else:
        return """
            <html><body>
            <h1>文件上传示例</h1>
            <form action="/upload" enctype='multipart/form-data' method='POST'>
                <input type="file" name="file">
                <input type="submit" value="上传">
            </form>
            </body></html>
        """
app.run(host="0.0.0.0", port=8888)