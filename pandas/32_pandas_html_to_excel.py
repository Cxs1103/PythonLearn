#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 32_pandas_html_to_excel.py
@Date  : 2021/12/5 15:27
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas借助Python爬虫读取HTML网页表格存储到Excel文件
实现目标：

网易有道词典可以用于英语单词查询，可以将查询的单词加入到单词本;
当前没有导出全部单词列表的功能。为了复习方便，可以爬取所有的单词列表，存入Excel方便复习
涉及技术：

Pandas：Python语言最强大的数据处理和数据分析库
Python爬虫：可以将网页下载下来然后解析，使用requests库实现，需要绕过登录验证
'''
import requests
import requests.cookies
import json
import time
import pandas as pd

"""
1. 登录网易有道词典的PC版，微信扫码登录，复制cookies到文件
PC版地址：http://dict.youdao.com/
Chrome插件可以复制Cookies为Json格式：http://www.editthiscookie.com/s
"""
cookie_jar = requests.cookies.RequestsCookieJar()

with open("./datas/read_html/cookie.txt") as fin:
    cookiejson = json.loads(fin.read())
    for cookie in cookiejson:
        cookie_jar.set(
            name=cookie["name"],
            value=cookie["value"],
            domain=cookie["domain"],
            path=cookie["path"]
        )
print(cookie_jar)

# 2. 将html都下载下来存入列表
htmls = []
url = "http://dict.youdao.com/wordbook/wordlist?p={idx}&tags="
for idx in range(6):
    time.sleep(1)
    print("**爬数据：第%d页" % idx)
    r = requests.get(url.format(idx=idx), cookies=cookie_jar)
    htmls.append(r.text)
print(htmls[0])

# 3. 使用Pandas解析网页中的表格
df = pd.read_html(htmls[0])
print(len(df))
print(type(df))


print(df[0].head(3))

# 序号	单词	音标	解释	时间	分类	操作
print(df[1].head(3))

df_cont = df[1]
df_cont.columns = df[0].columns
print(df_cont.head(3))

# 收集6个网页的表格
df_list = []
for html in htmls:
    df = pd.read_html(html)
    df_cont = df[1]
    df_cont.columns = df[0].columns
    df_list.append(df_cont)
# 合并多个表格
df_all = pd.concat(df_list)
print(df_all.head(3))

print(df_all.shape)

# 4. 将结果数据输出到Excel文件
df_all[["单词", "音标", "解释"]].to_excel("./course_datas/c32_read_html/网易有道单词本列表.xlsx", index=False)