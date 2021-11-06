#!/usr/bin/env python
# encoding: utf-8
'''
@File  : NoLockScreen.py.py
@Date  : 2021/10/23 0:23
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python控制电脑永不锁屏
'''

import pyautogui
import random
import time

while True:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    pyautogui.moveRel(x, y)
    time.sleep(5)