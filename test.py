#!/usr/bin/env python
# encoding: utf-8
'''
@File  : test.py
@Date  : 2021/11/1 22:00
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
class ParentClass(object):
    var = "test for parent"

    @classmethod
    def clsmethod(cls):
        print(cls.var)

class SubClass(ParentClass):
    var = "test for sub"

ParentClass.clsmethod()

SubClass.clsmethod()