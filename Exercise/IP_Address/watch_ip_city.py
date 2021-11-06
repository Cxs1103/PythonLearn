#!/usr/bin/env python
# encoding: utf-8
'''
@File  : watch_ip_city.py
@Date  : 2021/10/27 22:56
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python查询IP的地理位置
'''

import requests,json

def get_ip_localtion(ip):
    url = f"http://ip.taobao.com/outGetIpInfo?ip={ip}&accessKey=alibaba-inc"
    r = requests.get(url)
    data = json.loads(r.text)
    country, region, city, isp = (
        data["data"]["country"],
        data["data"]["region"],
        data["data"]["city"],
        data["data"]["isp"]
    )
    return country, region, city, isp

print(get_ip_localtion("61.152.197.156"))
print(get_ip_localtion("1.12.37.255"))
print(get_ip_localtion("211.161.240.166"))