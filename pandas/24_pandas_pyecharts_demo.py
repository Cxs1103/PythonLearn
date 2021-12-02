#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 24_pandas_pyecharts.py
@Date  : 2021/12/2 22:36
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas是Python用于数据分析领域的超级牛的库
Echarts是百度开源的非常好用强大的可视化图表库，Pyecharts是它的Python库版本
'''
from pyecharts.charts import Bar

# 首先开始来绘制你的第一个图表
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render('./datas/pyecharts/pyecharts_01.html')

# pyecharts 所有方法均支持链式调用。
bar = (
    Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 100, 75, 90])
)
bar.render('./datas/pyecharts/pyecharts_02.html')

# 使用 options 配置项，在 pyecharts 中，一切皆 Options。
from pyecharts.charts import Bar
from pyecharts import options as opts

# V1 版本开始支持链式调用
# 你所看到的格式其实是 `black` 格式化以后的效果
# 可以执行 `pip install black` 下载使用
bar = (
    Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 30, 75, 90])
        .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
bar.render('./datas/pyecharts/pyecharts_03.html')

# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 50, 75, 90])
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
bar.render('./datas/pyecharts/pyecharts_04.html')

# 渲染成图片文件，这部分内容请参考 进阶话题-渲染图片
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
# 需要下载chromediver，并放置到python安装目录
from snapshot_selenium import snapshot

bar = (
    Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 80, 75, 90])
)
make_snapshot(snapshot, bar.render('./datas/pyecharts/pyecharts_04.html'), "./datas/pyecharts/pyecharts_04.png")


# 使用主题
# pyecharts 提供了 10+ 种内置主题，开发者也可以定制自己喜欢的主题，进阶话题-定制主题 有相关介绍。

from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
)
bar.render('./datas/pyecharts/pyecharts_05.html')
# Note: 在使用 Pandas&Numpy 时，请确保将数值类型转换为 python 原生的 int/float。比如整数类型请确保为 int，而不是 numpy.int32

"""
使用 Notebook
当然你也可以采用更加酷炫的方式，使用 Notebook 来展示图表，matplotlib 有的，pyecharts 也会有的。pyecharts 支持 Jupyter Notebook / Jupyter Lab / Nteract / Zeppelin 四种环境的渲染。具体内容请参考 进阶话题/Notebook
"""