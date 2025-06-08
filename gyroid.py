import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-np.pi, np.pi, 100)
v = np.linspace(-np.pi, np.pi, 100)
u, v = np.meshgrid(u, v)
a = 1.0

x = a * np.sin(u)
y = a * np.sin(v)
z = a * np.sin(u + v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='spring', edgecolor='k', linewidth=0.1)
ax.set_title("Gyroid Patch (not implicit)")
plt.show()
