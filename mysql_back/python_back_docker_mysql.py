#!/usr/bin/env python
# encoding: utf-8
'''
@File  : python_back_docker_mysql.py
@Date  : 2021/10/29 16:51
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : python脚本备份docker容器中的mysql数据
'''
import datetime
import os

today = datetime.date.today()

databases = ['test']
host = 'localhost'
user = 'root'
password = '123456'
port = '3306'

mkdir_dir = f'/home/{today.strftime("%Y%m%d")}'
if not os.path.isdir(mkdir_dir):
    os.mkdir(mkdir_dir)

os.chdir(mkdir_dir)
for database_name in databases:
    sql_filename = database_name + '_' + today.strftime("%Y%m%d") + '.sql'
    sql_comm = "docker exec -it mysql mysqldump --skip-lock-tables --single-transaction --flush-logs --hex-blob -u%s -p%s --master-data=2 --opt %s > %s"%(user,password,database_name,sql_filename)
    if os.system(sql_comm) == 0:
        print(f'{database_name} 备份成功！')
    else:
        print(f'{database_name} 备份失败！请立即检查！！')