#!/usr/bin/env python
# encoding: utf-8
'''
@File  : imagerecognition.py
@Date  : 2021/10/28 12:54
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python实现图片验证码识别
'''
from PIL import Image
import pytesseract

path = '5809.jpg'
# path = 'chinese.png'

captcha = Image.open(path)

result = pytesseract.image_to_string(captcha)
# result = pytesseract.image_to_string(captcha, lang='chi_sim')

print(result)
