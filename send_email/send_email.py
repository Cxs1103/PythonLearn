#!/usr/bin/env python
# encoding: utf-8
'''
@File  : send_email.py
@Date  : 2021/11/7 19:06
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''

import smtplib
from email.header import Header
from email.mime.text import MIMEText


def my_send_email(title, content_html, from_email, to_email):
    # 邮件内容
    message = MIMEText(content_html, 'html', 'utf-8')

    # 邮件信息
    message['Subject'] = Header(title, 'utf-8')
    message['From'], message['To'] = from_email, to_email

    # 使用163邮箱的服务发送邮件
    smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)
    smtpObj.login(from_email,'KNGDVJZPXSWAWZWSZVVYE')
    smtpObj.sendmail(from_email,[to_email],message.as_string())
    smtpObj.quit()


my_send_email("标题：来自Python的测试邮件",
              "<h1>内容： Python测试邮件</h1>",
              "cxs1103@163.com", "cxs1103@163.com")
