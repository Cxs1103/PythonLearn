#!/usr/bin/env python
# encoding: utf-8
'''
@File  : app.py
@Date  : 2021/10/28 23:12
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : flask app 注册
'''

from flask import Flask

from English_translate.english_dict import english_dict
from English_translate.default_blueprint import dft_blueprint

app = Flask(__name__)

app.register_blueprint(dft_blueprint)
english_dict.load_data("./mydict/stardict.csv")

app.run()