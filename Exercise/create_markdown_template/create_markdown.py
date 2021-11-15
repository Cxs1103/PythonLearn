#!/usr/bin/env python
# encoding: utf-8
'''
@File  : create_markdown.py
@Date  : 2021/11/15 22:48
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : 
'''
import os
import time

os.chdir(r'./datas')


def main():
    # 创建文件夹
    today_date = time.strftime('%Y%m%d', time.localtime())
    file_path = os.getcwd() + '/{}'.format(today_date)
    # print(today_date, file_path)

    if os.path.exists(file_path):
        raise ValueError('🚨工作记录文件夹已存在：{}'.format(file_path))
    else:
        print('文件夹已生成✔')

    # 模板内容
    template = """# {} 工作记录 
1.
2.
3.
	""".format(time.strftime('%Y/%m/%d'), time.localtime())
    print('✨✨✨✨✨ 模板内容生成！✨✨✨✨✨')
    print(template)

    # 创建模板文档
    with open(r'{}工作记录.md'.format(today_date), 'w+', encoding='utf-8') as fin:
        fin.write(template)
    print('✨✨✨✨✨ 记录文件路径生成完毕！✨✨✨✨✨')
    print(file_path)

if __name__ == '__main__':
    main()
