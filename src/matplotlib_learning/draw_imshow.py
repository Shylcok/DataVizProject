import numpy as np
import matplotlib.pyplot as plt


# 灰度图
def f(x_, y_): 
    return (1 - x_ / 2 + x_ ** 5 + y_ ** 3) * np.exp(-x_ ** 2 - y_ ** 2)


n = 10
x = np.linspace(-3, 3, 4 * n)
y = np.linspace(-3, 3, 3 * n)
X, Y = np.meshgrid(x, y)
plt.imshow(f(X, Y))
plt.show()
