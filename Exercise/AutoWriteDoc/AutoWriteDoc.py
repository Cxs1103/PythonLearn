#!/usr/bin/env python
# encoding: utf-8
'''
@File  : AutoWriteDoc.py
@Date  : 2021/10/23 10:39
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python控制电脑自动写文档
'''

content = "除此之外，它还是史上第一部同时拿下雨果奖和星云奖双料大奖的科幻巨著！是《轨迹》杂志评选的20世纪最佳科幻小说。就连科幻三巨头之一的阿瑟·克拉克都放话：除了《指环王》，没有作品能与它比肩！猜到没！集这么多牛逼荣誉于一身的，就是大名鼎鼎的科幻巨著《沙丘》！图片正好最近电影版《沙丘》上映，而书单狗看到不少人评价，和气势恢宏的原著相比，电影甚至都无法展现它十分之一的魅力！那今天就让书单狗带大家好好见识一下，原著到底是多么伟大的存在！图片不是吹，这套书绝对是书单狗心目中少有的，把广度和深度都做到登峰造极的科幻作品！"

import time
import pyautogui
import pyperclip

time.sleep(5)

pyautogui.click(600, 400)

for s in content:
    print(s)
    pyperclip.copy(s)
    pyautogui.hotkey('ctrl', 'v')
