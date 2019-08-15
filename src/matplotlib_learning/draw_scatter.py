import numpy as np
import matplotlib.pyplot as plt

# 散点图
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

plt.scatter(X, Y)
plt.show()
