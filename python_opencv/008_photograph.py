#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 008_photograph.py
@Date  : 2021/11/7 14:57
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
# 导入cv模块
import cv2.cv2 as cv

# 读取摄像头
cap = cv.VideoCapture(0)

flag = 1
num = 1

while (cap.isOpened()):  # 检测摄像头是否开启
    ret_flag, Vshow = cap.read()  # 获取每一帧图像
    cv.imshow("Capture_Test", Vshow)  # 显示图像
    k = cv.waitKey(1) & 0xFF  # 按键判断
    if k == ord('s'):
        cv.imwrite('C:/Users/Cxs/PycharmProjects/PythonLearn/python_opencv/' + str(num) + '.name' + '.jpg', Vshow)
        print("success to save" + str(num) + '.jpg')
        print('-------------------------------')
        num += 1
    elif k == ord(' '):
        break

# 释放摄像头
cap.release()

# 释放内存
cv.destroyAllWindows()
