#!/usr/bin/env python
# encoding: utf-8
'''
@File  : ExcelWebPivot.py
@Date  : 2021/10/26 23:54
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import flask
import pandas as pd

app= flask.Flask(__name__)

@app.route("/excel")
def show_excel():
    df = pd.read_excel("数据透视.xlsx")
    df_pivot = pd.pivot_table(df,
                              index=["日期", "公司"],
                              columns="数据项",
                              values="数据值"
                              )
    return f"""
        <html>
            <body>
                <h1>汇总统计</h1>
            %s
            <body>
        </html>
    """ % df_pivot.to_html()
app.run()

