#!/usr/bin/env python
# encoding: utf-8
'''
@File  : AutoScreenshot.py
@Date  : 2021/10/23 11:06
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python自动截屏
'''

import time
import pyautogui
import datetime
import socket
import os
import requests

image_dir = "./screenshot"

while True:
    curr_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    image_file = f"{image_dir}/image_{curr_time}.png"
    print(socket.gethostname(), "save images:", image_file)
    pyautogui.screenshot(image_file)
    time.sleep(5)

    # 发送给服务器
    url = "http://192.168.0.102:8888/upload_images"
    image_files = {'file':open(image_file, "rb")}
    r = requests.post(url, files=image_files, timeout=10)
    image_files['file'].close()
    os.remove(image_file)