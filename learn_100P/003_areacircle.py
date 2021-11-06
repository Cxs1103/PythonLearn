#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 003_areacircle.py
@Date  : 2021/11/1 22:40
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import math


def compute_area_circle(r):
    return round(math.pi * r * r, 2)


print("area of 2 is :", compute_area_circle(2))
print("area of 5 is :", compute_area_circle(5))
print("area of 10.12 is :", compute_area_circle(10.12))
