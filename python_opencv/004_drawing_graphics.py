#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 004_drawing_graphics.py
@Date  : 2021/11/7 12:00
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
# 导入cv模块
import cv2.cv2 as cv

# 读取图片
img = cv.imread('./picture/20211107110136.png')

# 坐标
x, y, w, h = 100, 100, 100, 100

# 绘制矩形
cv.rectangle(img, (x, y, x + w, y + h), color=(0, 0, 255), thickness=1)

# 绘制圆形
cv.circle(img, center=(x + w, y + h), radius=100, color=(255, 0, 0), thickness=2)

# 显示

cv.imshow('re_img', img)

# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
