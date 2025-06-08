import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2, 2, 100)
v = np.linspace(-2, 2, 100)
u, v = np.meshgrid(u, v)

x = u
y = v
z = np.log(np.cosh(v) / np.cosh(u))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='PuOr', edgecolor='k', linewidth=0.1)
ax.set_title("Scherk's Minimal Surface")
plt.show()
