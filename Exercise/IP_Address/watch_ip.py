#!/usr/bin/env python
# encoding: utf-8
'''
@File  : watch_ip.py
@Date  : 2021/10/27 22:41
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python获取自己电脑的外网IP地址
'''
import requests,json

r = requests.get("http://httpbin.org/ip").text

print(r)

ip = json.loads(r)["origin"]

print(ip)