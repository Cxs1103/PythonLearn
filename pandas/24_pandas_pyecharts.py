#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 24_pandas_pyecharts.py
@Date  : 2021/12/2 22:36
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas怎样结合Pyecharts绘制交互性折线图？
背景：
Pandas是Python用于数据分析领域的超级牛的库
Echarts是百度开源的非常好用强大的可视化图表库，Pyecharts是它的Python库版本
'''
# 1、读取数据
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

xlsx_path = './datas/stocks/baidu_stocks.xlsx'
df = pd.read_excel(xlsx_path, index_col="datetime", parse_dates=True)
print(df.head())
print(df.index)

df.sort_index(inplace=True)
print(df.head())

# 2、使用Pyecharts绘制折线图
# 如果没有安装，使用pip install pyecharts安装

# 折线图
line = Line()

# x轴
line.add_xaxis(df.index.to_list())

# 每个y轴
line.add_yaxis("开盘价", df["open"].round(2).to_list())
line.add_yaxis("收盘价", df["close"].round(2).to_list())

# 图表配置
line.set_global_opts(
    title_opts=opts.TitleOpts(title="百度股票2019年"),
    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
)
line.render("./datas/stocks/baidu_stocks.html")
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")

# Jupyter Notebook使用方式：
# line.render_notebook()

# from pyecharts.charts import Bar
#
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()
