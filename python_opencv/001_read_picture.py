#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 001_read_picture.py
@Date  : 2021/11/7 10:49
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread('./picture/20211107110136.png')

# 显示图片
cv.imshow('read_img',img)

# 等待
cv.waitKey(0)

#释放内存
cv.destroyAllWindows()