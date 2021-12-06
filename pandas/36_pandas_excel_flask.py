#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 36_pandas_excel_flask.py
@Date  : 2021/12/6 22:06
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas读取Excel将数据展示在网页上
'''

from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/')
def show_excel():
    df = pd.read_excel('./datas/vlookup/学生信息表.xlsx')
    table_html = df.to_html()
    return f"""
        <html>
            <boby>
                <h1>学生信息表</h1>
                <div>{table_html}</div>
            </boby>
        </html>
    """


if __name__ == '__main__':
    app.run(host="0.0.0.0")
