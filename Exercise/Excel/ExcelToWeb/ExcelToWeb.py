#!/usr/bin/env python
# encoding: utf-8
'''
@File  : ExcelToWeb.py
@Date  : 2021/10/26 23:38
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python在网页上展示Excel文件
'''
import flask
import pandas as pd

app= flask.Flask(__name__)

@app.route("/excel")
def show_excel():
    df = pd.read_excel("汇总统计.xlsx")
    return f"""
        <html>
            <body>
                <h1>汇总统计</h1>
            %s
            <body>
        </html>
    """ % df.to_html()
app.run()