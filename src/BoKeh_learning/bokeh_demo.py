#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: bokeh_demo.py
@time: 2019/8/15 17:18
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
# 导入图表绘制、图标展示模块

from bokeh.io import output_notebook
# 导入notebook绘图模块
import warnings

warnings.filterwarnings('ignore')
# 不发出警告
# 在notebook中创建绘图空间


output_notebook()
# notebook绘图命令

p = figure(plot_width=400, plot_height=400)  # 创建图表，设置宽度、高度
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
# 创建一个圆形散点图

show(p)
# 绘图
