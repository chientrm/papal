import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1.5, 1.5, 50)
u, v = np.meshgrid(u, v)
a = 1

x = a * np.cosh(v) * np.cos(u)
y = a * np.cosh(v) * np.sin(u)
z = a * v

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='winter', edgecolor='k', linewidth=0.1)
ax.set_title("Catenoid")
plt.show()
