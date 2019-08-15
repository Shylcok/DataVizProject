import numpy as np
import matplotlib.pyplot as plt

plt.axes([0, 0, 1, 1])
# 极轴图
plt.figure(figsize=(8, 4))

ax1 = plt.subplot(111, projection='polar')
ax1.set_title('radar map\n')  # 创建标题
ax1.set_rlim(0, 12)

data1 = np.random.randint(1, 10, 10)
data2 = np.random.randint(1, 10, 10)
data3 = np.random.randint(1, 10, 10)
theta = np.arange(0, 2 * np.pi, 2 * np.pi / 10)
# 创建数据

ax1.plot(theta, data1, '.--', label='data1')
ax1.fill(theta, data1, alpha=0.2)
ax1.plot(theta, data2, '.--', label='data2')
ax1.fill(theta, data2, alpha=0.2)
ax1.plot(theta, data3, '.--', label='data3')
ax1.fill(theta, data3, alpha=0.2)

plt.show()
