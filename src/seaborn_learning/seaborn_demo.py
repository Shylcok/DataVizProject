#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: seaborn_demo.py
@time: 2019/8/15 17:19
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import seaborn as sns

s1 = Series(np.random.randn(1000))  # 生成1000个点的符合正态分布的随机数
plt.hist(s1)  # 直方图，也可以通过plot(),修改里面kind参数实现
s1.plot(kind='kde')  # 密度图
