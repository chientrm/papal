import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2, 2, 100)
v = np.linspace(-2, 2, 100)
u, v = np.meshgrid(u, v)

x = u
y = u * v
z = v**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='cubehelix', edgecolor='k', linewidth=0.1)
ax.set_title("Whitney Umbrella")
plt.show()
