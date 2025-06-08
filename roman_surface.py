import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

x = np.sin(u) * np.cos(v)
y = np.sin(u) * np.sin(v)
z = np.cos(u)
# Roman surface parametric equations
X = x * y
Y = y * z
Z = z * x

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='cividis', edgecolor='k', linewidth=0.1)
ax.set_title("Roman Surface")
plt.show()
