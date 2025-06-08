import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0.01, 4 * np.pi, 100)
v = np.linspace(0.01, 1, 50)
u, v = np.meshgrid(u, v)
a = 1
b = 0.2

x = a * np.cos(u) * np.sin(v)
y = a * np.sin(u) * np.sin(v)
z = a * (np.cos(v) + np.log(np.tan(v / 2))) + b * u

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='magma', edgecolor='k', linewidth=0.1)
ax.set_title("Dini's Surface")
plt.show()
