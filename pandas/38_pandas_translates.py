#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 38_pandas_translates.py
@Date  : 2021/12/7 21:03
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :

Python批量翻译英语单词
用途：
对批量的英语文本，生成英语-汉语翻译的单词本，提供Excel下载

本代码实现：

提供一个英文文章URL，自动下载网页；
实现网页中所有英语单词的翻译；
下载翻译结果的Excel
涉及技术：

pandas的读取csv、多数据merge、输出Excel
requests库下载HTML网页
BeautifulSoup解析HTML网页
Python正则表达式实现英文分词
1. 读取英语-汉语翻译词典文件
词典文件来自：https://github.com/skywind3000/ECDICT 使用步骤：

下载代码打包：https://github.com/skywind3000/ECDICT/archive/master.zip
解压master.zip，然后解压其中的‪stardict.csv文件
'''
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

df_dict = pd.read_csv("./datas/chinese_english/stardict.csv")
print(df_dict.head())

print(df_dict.shape)

print(df_dict.sample(10).head())

# 把word、translation之外的列扔掉
df_dict = df_dict[["word", "translation"]]
print(df_dict.head())

# 2. 下载网页，得到网页内容
import requests

# Pandas官方文档中的一个URL
url = "https://pandas.pydata.org/docs/user_guide/indexing.html"

html_cont = requests.get(url).text
print(html_cont[:100])

# 3. 提取HTML的正文内容
# 即：去除HTML标签，获取正文

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_cont, features="html.parser")
html_text = soup.get_text()
print(html_text[:500])

# 4. 英文分词和数据清洗
# 分词
import re

word_list = re.split("""[ ,.\(\)/\n|\-:=\$\["']""", html_text)
print(word_list[:10])

# 读取停用词表，从网上复制的，位于当前目录下
with open("./datas/chinese_english/stop_words.txt") as fin:
    stop_words = set(fin.read().split("\n"))
print(list(stop_words)[:10])

# 数据清洗
word_list_clean = []
for word in word_list:
    word = str(word).lower().strip()

    # 过滤掉空词，数字，单个字符，停用词
    if not word or word.isnumeric() or len(word) <= 1 or word in stop_words:
        continue
    word_list_clean.append(word)
print(word_list_clean[:20])

# 5. 分词结果构造成一个DataFrame
df_words = pd.DataFrame({
    "word": word_list_clean
})
print(df_words)

# 统计词频
df_words = (
    df_words
        .groupby("word")["word"]
        .agg(count='size')
        .reset_index()
        .sort_values(by='count', ascending=False)
)
print(df_words.head(10))

# 6. 和单词词典实现merge
df_merge = pd.merge(
    left=df_dict,
    right=df_words,
    left_on="word",
    right_on="word"
)
print(df_merge.sample(10))
print(df_merge.shape)

# 7. 存入Excel
df_merge.to_excel("./datas/chinese_english/batch_chinese_english.xlsx", index=False)

"""
后续升级：
可以提供txt/excel/word/pdf的批量输入，生成单词本；
可以做成网页、微信小程序的形式，在线访问和使用
用户可以标记或上传“已经认识的词语”，每次过滤掉
"""