#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 005_face_detection.py
@Date  : 2021/11/7 12:50
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
# 导入cv模块
import cv2.cv2 as cv


# 人脸检测函数
def face_detect_demo():
    gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier(
        'D:/Program Files/Python3.7/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gary, 1.059, 5, 0, (10, 10), (100, 100))  # 但是这个参数只适用于这张照片
    # face = face_detect.detectMultiScale(gary)  # 默认会有偏差
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)


# 读取图片
# img = cv.imread('./datas/pictures/20211107110136.png')
img = cv.imread('./datas/pictures/20211107130231.png')

# 调用检测函数
face_detect_demo()

# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
