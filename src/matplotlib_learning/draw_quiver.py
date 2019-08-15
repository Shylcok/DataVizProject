import numpy as np
import matplotlib.pyplot as plt

# 量场图
n = 8
X, Y = np.mgrid[0:n, 0:n]
plt.quiver(X, Y)
plt.show()
