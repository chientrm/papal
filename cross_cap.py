import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

x = np.sin(u) * np.sin(2 * v) / 2
y = np.sin(2 * u) * np.cos(v) ** 2
z = np.cos(u) * np.sin(2 * v) / 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='YlGnBu', edgecolor='k', linewidth=0.1)
ax.set_title("Cross-cap")
plt.show()
