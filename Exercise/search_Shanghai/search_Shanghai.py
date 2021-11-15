#!/usr/bin/env python
# encoding: utf-8
'''
@File  : search_Shanghai.py
@Date  : 2021/11/15 23:19
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import requests
from bs4 import BeautifulSoup

url = 'http://www.tcmap.com.cn/shanghai/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

response = requests.get(url, headers=headers)  # 发送HTTP请求
response.encoding = 'gb18030'  # 设置一下网站的中文编码
soup = BeautifulSoup(response.text, 'html.parser')  # 使用 BeautifulSoup 进行解析
# print(soup)
streets = []

# 找到数据对应的 html 节点，然后使用get_text()函数获取
for street in soup.find_all('a', class_='blue'):
    streets.append(street.get_text())

# 最后写入到相关文件夹中
with open(r'./address.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(streets[:238]))
