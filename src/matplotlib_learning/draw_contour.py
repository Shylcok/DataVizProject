import numpy as np
import matplotlib.pyplot as plt


def f(x_, y_):
    return (1 - x_ / 2 + x_ ** 5 + y_ ** 3) * np.exp(-x_ ** 2 - y_ ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
plt.show()
