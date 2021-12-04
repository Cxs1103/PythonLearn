#!/usr/bin/env python
# encoding: utf-8
'''
@File  : WebFindExcel.py
@Date  : 2021/10/26 23:58
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python制作网页，查询Excel数据
'''
import flask
import pandas as pd
from flask import request

app = flask.Flask(__name__)

@app.route("/query_grade", methods=["POST", "GET"])
def query_grade():
    df = pd.read_excel("../Exercise/WebFindExcel/学生成绩表.xlsx")

    grade_data = pd.DataFrame()
    student_name = request.form.get("student_name", "")
    if student_name:
        grade_data = df.query(f"姓名 == '{student_name}'")

    return f"""
        <html><body style="text-align:center">
            <h1>查询学生成绩</h1>
            <form action="/query_grade" method="post">
                姓名：<input type="text" name="student_name" value="{student_name}">
                <input type="submit" name="submit" value="查询">
            </form>
            <center> %s </center>
        </body></html>
    """ % grade_data.to_html(index=False)
app.run()
