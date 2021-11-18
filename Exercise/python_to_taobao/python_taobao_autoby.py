#!/usr/bin/env python
# encoding: utf-8
'''
@File  : python_taobao_autoby.py
@Date  : 2021/11/19 0:21
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

from selenium import webdriver
import datetime
import time


def login():
    # 打开浏览器
    browser.get('https://www.taobao.com')

    # 等待页面加载3秒
    time.sleep(3)

    if browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[1]/li[2]/div[1]/div[1]/a[1]'):
        browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[1]/li[2]/div[1]/div[1]/a[1]').click()
        browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div/div[1]/i').click()

        # 等待10秒内进行扫码
        time.sleep(10)

        # 打开购物车
        # browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[2]/li[3]/div[1]/a/span[2]').click()
        # or
        browser.get('https://cart.taobao.com/cart.htm')

    time.sleep(3)

    # 记录打开购物车时间
    open_time = datetime.datetime.now()
    print('login success：', open_time.strftime("%Y-%m-%d %H:%M:%S"))


# 购买操作
def buy(times):
    # 死循环
    while True:
        buy_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        # 时间对比
        if buy_time >= times:
            while True:
                try:
                    if browser.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div'):
                        browser.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div').click()
                        break
                except:
                    print('找不到全选按钮')

            # 结算
            while True:
                try:
                    if browser.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div[3]/div[5]/a/span'):
                        browser.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div[3]/div[5]/a/span').click()
                        print('结算成功')
                        break
                except:
                    pass

            # 提交订单
            while True:
                try:
                    if browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[24]/div/div[1]/a[2]'):
                        browser.find_element_by_xpath(
                            '/html/body/div[2]/div[1]/div[1]/div/div[24]/div/div[1]/a[2]').click()
                        order_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print('抢购成功，时间为：', order_time)
                        break

                except:
                    print('再次尝试提交订单')
                time.sleep(0.01)


if __name__ == '__main__':
    browser = webdriver.Firefox(executable_path='./geckodriver.exe')
    times = input('请输入抢购时间，格式为:2021-11-19 01:55:00.000000:')
    login()
    buy(times)
