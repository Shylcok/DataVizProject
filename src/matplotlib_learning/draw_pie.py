import numpy as np
import matplotlib.pyplot as plt

# 饼状图
n = 20
Z = np.random.uniform(0,1,n)
plt.pie(Z)
plt.show()
