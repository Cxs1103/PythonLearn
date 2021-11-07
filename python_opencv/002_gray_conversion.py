#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 002_gray_conversion.py
@Date  : 2021/11/7 11:05
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
# 导入cv模块
import cv2.cv2 as cv

# 读取图片
img = cv.imread('./datas/pictures/20211107110136.png')

#灰度转换
gray_img= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 显示灰阶图片
cv.imshow('gray_img',gray_img)

cv.imwrite('./datas/gray_img.jpg',gray_img)

# 显示图片
cv.imshow('read_img',img)

# 等待
cv.waitKey(0)

#释放内存
cv.destroyAllWindows()