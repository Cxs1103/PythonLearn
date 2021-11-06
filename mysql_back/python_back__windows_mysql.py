#!/usr/bin/env python
# encoding: utf-8
'''
@File  : python_back_docker_mysql.py
@Date  : 2021/10/29 16:51
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : python脚本备份windows下mysql数据
'''
import datetime
import os

today = datetime.date.today()

databases = ['students']
host = 'localhost'
user = 'root'
password = '123456'
port = '3306'

mkdir_dir = f'./{today.strftime("%Y%m%d")}'
print(mkdir_dir)
if not os.path.isdir(mkdir_dir):
    os.mkdir(mkdir_dir)

os.chdir(mkdir_dir)
for database_name in databases:
    sql_filename = database_name + '_' + today.strftime("%Y%m%d") + '.sql'
    mysqldump_path = r'"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe"'
    sql_comm = f"{mysqldump_path} --skip-lock-tables --single-transaction --flush-logs --hex-blob -u%s -p%s --master-data=2 --opt %s > %s" % (
    user, password, database_name, sql_filename)
    if os.system(sql_comm) == 0:
        print(f'{database_name} 备份成功！')
    else:
        print(f'{database_name} 备份失败！请立即检查！！')
