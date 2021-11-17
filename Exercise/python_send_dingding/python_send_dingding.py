#!/usr/bin/env python
# encoding: utf-8
'''
@File  : python_send_dingding.py
@Date  : 2021/11/18 0:27
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse

timestamp = int(round(time.time() * 1000))
secret = 'SEC714XXXXXXXXXXXXXXX'
secret_enc = bytes(secret.encode("utf-8"))
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = bytes(string_to_sign.encode('utf-8'))
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)


def dingmessage():
    # 请求的URL，WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=3f556e31dXXXXXXXXXXXXXXXXX&timestamp={timestamp}&sign={sign}'.format(
        timestamp=timestamp, sign=sign)

    # 构建请求头部
    header = {"Content-Type": "application/json", "Charset": "UTF-8"}

    # 构建请求数据
    message = {
        "msgtype": "link",
        "link": {
            "text": "这只是一个测试内容！！",
            "title": "这只是一个测试标题",
            "picUrl": "http://mmbiz.qpic.cn/sz_mmbiz_jpg/h9sUcMMuUlfTlXnVP6NyFVExMJ4jCHia70zZQfBEZ9PeSrH3IGMRWDyqMoh3TOXgbZHSmTZm8utFbcdheWDc0EQ/0?wx_fmt=jpeg",
            # "messageUrl": "https://www.dingtalk.com",
            # "messageUrl": "https://www.baidu.com",
            "messageUrl": "https://www.bilibili.com",
        }
    }

    # 对请求的数据进行json封装
    message_json = json.dumps(message)

    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)

    # 打印返回的结果
    print(info.text)


if __name__ == "__main__":
    dingmessage()
