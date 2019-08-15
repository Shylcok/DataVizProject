#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: demo.py
@time: 2019/8/15 14:21
"""
import matplotlib.pyplot as plt
import numpy as np

# 创建一个 10 * 6 点（point）的图，并设置分辨率为 80
plt.figure(figsize=(10, 6), dpi=80)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # x轴的取值范围从-π到π，然后是
C, S = np.cos(X), np.sin(X)  # y的取值函数

# 分别绘制图像
# 其中前两个参数不变，color参数为线条颜色，line_width为线条宽度（像素），line_style为线条样式
# plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
# plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")
# 添加图例在 plt.plot的参数中添加label参数并赋值为图例名称即可
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")
# 添加图例并设置图例位置
plt.legend(loc='upper left')

# 绘制图片边界
xmin, xmax = X.min(), X.max()
ymin, ymax = C.min(), C.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
# xlim 和 ylim是在设置x、y轴的上下限
# 因为正余弦的值域相同所以上面y取C或者S均可
plt.xlim(xmin - dx, xmax + dx)
plt.ylim(ymin - dy, ymax + dy)

# 设置记号
# xticks 和 yticks是在设置x、y轴的记号
# 也就是对应的特殊点对应在x,y轴的对应位置
# plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
# plt.yticks([-1, 0, +1])
# 优化标记
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

# 移动脊柱
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 添加特殊点的注释
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
# plt.scatter同来绘制散点图
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
# 使用LaTeX用来写注释
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 图像优化
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

# 显示图像
plt.show()
# plt.savefig(r'C:\Users\11985\Pictures\Saved Pictures\a.jpg')

