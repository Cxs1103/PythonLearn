#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 003_change_size.py
@Date  : 2021/11/7 11:42
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
# 导入cv模块
import cv2.cv2 as cv

# 读取图片
img = cv.imread('./picture/20211107110136.png')

# 修改图片大小
resize_img = cv.resize(img, dsize=(600, 375))

# 显示原图片
cv.imshow('read_img', img)

# 修改后的图片
cv.imshow('resize_img', resize_img)

# 显示图片原尺寸
print('未修改', img.shape)
# 显示修改后的尺寸
print('未修改', resize_img.shape)

# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
