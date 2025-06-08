import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2 * np.pi, 2 * np.pi, 100)
v = np.linspace(-2, 2, 50)
u, v = np.meshgrid(u, v)

x = v * np.cos(u)
y = v * np.sin(u)
z = u

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='autumn', edgecolor='k', linewidth=0.1)
ax.set_title("Helicoid")
plt.show()
