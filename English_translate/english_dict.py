#!/usr/bin/env python
# encoding: utf-8
'''
@File  : english_dict.py
@Date  : 2021/10/29 0:14
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 翻译字典模块
'''
import pandas as pd

# dict_path = "./mydict/stardict.csv"
class EnglishDict():
    def __int__(self):
        self.data_dict = None

    def load_data(self, dict_path):
        self.data_dict = pd.read_csv(dict_path, usecols=["word", "translation"])

    def query(self, word):
        row = self.data_dict.query(f"word == '{word}'")
        if row is not None:
            return row.iloc[0]["translation"]
        return "没有查询到结果"

english_dict = EnglishDict()