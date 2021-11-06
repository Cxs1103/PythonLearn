#!/usr/bin/env python
# encoding: utf-8
'''
@File  : RemoteControlMusic.py
@Date  : 2021/10/24 23:33
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  : Python用手机远程控制电脑播放歌曲
'''

import os,random
from flask import Flask

app = Flask(__name__)

music_dir = "C:\CloudMusic"

@app.route('/music')
def music():
    music_files = [file for file in os.listdir(music_dir)
                    if file.endswith(".mp3")]
    music_file = random.choice(music_files)
    #os.system(f'open"{music_dir}/{music_file}"') Mac
    os.system(f'start "{music_dir}/{music_file}"') # windows
    return "<br/>"*10 + f"""<h1>当前播放<br/>{music_file}</h1>"""

app.run(host="0.0.0.0", port=8888)