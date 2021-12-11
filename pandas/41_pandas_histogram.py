#!/usr/bin/env python
# encoding: utf-8
'''
@File  : 41_pandas_histogram.py
@Date  : 2021/12/11 16:31
@Author: Cxs
@Email: Cxs1103@163.com
@Desc  :
Pandas读取Excel绘制直方图
直方图(Histogram)：
直方图是数值数据分布的精确图形表示，是一个连续变量（定量变量）的概率分布的估计，它是一种条形图。
为了构建直方图，第一步是将值的范围分段，即将整个值的范围分成一系列间隔，然后计算每个间隔中有多少值。
'''
# 1. 读取数据
# 波斯顿房价数据集
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 1000)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 1000)

df = pd.read_excel("./datas/boston-house-prices/housing.xlsx")
print(df.head())
print(df.info())

print(df["MEDV"])

# 2. 使用matplotlib画直方图
# matplotlib直方图文档：https://matplotlib.org/3.2.0/api/_as_gen/matplotlib.pyplot.hist.html
plt.figure(figsize=(12, 5))
plt.hist(df["MEDV"], bins=100)
# plt.show()

# 3. 使用pyecharts画直方图
# pyecharts直方图文档：http://gallery.pyecharts.org/#/Bar/bar_histogram
# numpy直方图文档：https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html
from pyecharts import options as opts
from pyecharts.charts import Bar

# 需要自己计算有多少个间隔、以及每个间隔有多少个值
hist, bin_edges = np.histogram(df["MEDV"], bins=100)
# 这是每个间隔的分割点
print(f'间隔的分割点:{bin_edges}')
# 这是每个间隔的分割点数量
print(len(bin_edges))
# 这是间隔的计数
print(f'间隔的计数:{hist}')
# 这是间隔计数的数量
print(len(hist))

# 对bin_edges的解释，为什么是101个？比hist计数多1个？
# 举例：如果bins是[1, 2, 3, 4]，那么会分成3个区间：[1, 2)、[2, 3)、[3, 4]；
# 其中bins的第一个值是数组的最小值，bins的最后一个元素是数组的最大值

# 注意观察，min是bins的第一个值，max是bins的最后一个元素
print(df["MEDV"].describe())

# 查看bins每一个值和前一个值的差值，可以看到这是等分的数据
print(np.diff(bin_edges))

# 这些间隔的数目，刚好等于计数hist的数目
print(len(np.diff(bin_edges)))

# pyecharts的直方图使用bar实现
# 取bins[:-1]，意思是用每个区间的左边元素作为x轴的值
bar = (
    Bar()
        .add_xaxis([str(x) for x in bin_edges[:-1]])
        .add_yaxis("价格分布", [float(x) for x in hist], category_gap=0)
        .set_global_opts(
        title_opts=opts.TitleOpts(title="波斯顿房价-价格分布-直方图", pos_left="center"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)
bar.render('./datas/boston-house-prices/huosing.html')
# 小作业：
# 获取你们产品的销量数据、价格数据，提取得到一个一数组，画一个直方图看一下数据分布