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
import time

today = datetime.date.today()
# oneday = datetime.timedelta(days=1)
# deleteday = 10
# print(deleteday)

databases = ['test', 'jira']
sql_host = 'localhost'
sql_user = 'root'
sql_password = '123456'
sql_port = '3306'

# 创建备份目录
back_dir = '/home/mysql/'
mkdir_dir = f'{back_dir}{today.strftime("%Y%m%d")}'
if not os.path.isdir(mkdir_dir):
    os.mkdir(mkdir_dir)

# 备份文件
os.chdir(mkdir_dir)
for database_name in databases:
    sql_filename = database_name + '_' + today.strftime("%Y%m%d") + '.sql'
    sql_comm = "/usr/local/mysql/bin/mysqldump --skip-lock-tables --single-transaction --flush-logs --hex-blob -u%s -p%s -P%s -h%s --master-data=2 --opt %s > %s" % (
    sql_user, sql_password, sql_port, sql_host, database_name, sql_filename)
    if os.system(sql_comm) == 0:
        print(f'{database_name} 备份成功！')
        tar_filename = database_name + '_' + today.strftime("%Y%m%d") + '.tar.gz'
        tar_comm = "tar -zcf %s %s" % (tar_filename, sql_filename)
        if os.system(tar_comm) == 0:
            print(f'{database_name} 打包成功！')
        else:
            print(f'{database_name} 打包失败，请立即检查！！')
    else:
        print(f'{database_name} 备份失败，请立即检查！！')

# 远程服务器信息
scp_host = '192.168.0.81'
scp_user = 'root'
scp_port = '22206'
scp_dir = '/home/'

# scp传输备份文件
for backfile in os.listdir(mkdir_dir):
    if backfile.endswith(".tar.gz"):
        scp_comm = "scp -P%s %s %s@%s:%s" % (scp_port, backfile, scp_user, scp_host, scp_dir)
        if os.system(scp_comm) == 0:
            print(f'{backfile} 已传输到备份服务器')
        else:
            print("传输到备份服务器失败")

# 删除10天前的历史备份文件
deleteday = 10

# 方法三
bretime = time.time() - 3600 * 24 * deleteday
print(bretime)
for file in os.listdir(back_dir):
    filename = back_dir + os.sep + file
    if os.path.getmtime(filename) < bretime:
        try:
            if os.path.isfile(filename):
                os.remove(filename)
            elif os.path.isdir(filename):
                os.removedirs(filename)
            else:
                os.remove(filename)
            print("%s remove success." % filename)
        except Exception as error:
            print('error')
            print("%s remove faild." % filename)

# 方法一
# for backfiles in os.listdir(back_dir):
#     backfile_time = os.path.getctime(os.path.join(back_dir, backfiles))
#     calc_time = (datetime.datetime.now() - datetime.timedelta(days=deleteday)).timestamp()
#     if backfile_time < calc_time:
#         rm_comm = "rm -rf %s"%(backfiles)
#         os.system(rm_comm)

# 方法二
# deleteday = 10
# find_delete_file = "find %s* -mtime -%s"%(back_dir, deleteday)
# result = os.popen(find_delete_file).read()
# delete_files = []
# for delete_file in result.splitlines():
#     print(delete_file)
#     delet_comm = "rm -rf %s"%(delete_file)
#     if os.system(delet_comm) == 0:
#         print(f'{delete_file} 已删除！')
#     else:
#         print(f'{delete_file} 删除失败！')