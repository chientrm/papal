import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0, np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Parametric equations for Boy's surface (projective plane immersion)
x = (1/2) * (np.cos(u) * np.cos(u) * np.cos(2*v) + np.sqrt(2) *
             np.cos(u) * np.sin(u) * np.cos(v) + np.sin(u) * np.sin(u))
y = (1/2) * (np.cos(u) * np.cos(u) * np.sin(2*v) - np.sqrt(2) *
             np.cos(u) * np.sin(u) * np.sin(v) + np.sin(u) * np.sin(u))
z = np.sqrt(3)/2 * np.cos(u) * np.sin(u)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='plasma', edgecolor='k', linewidth=0.1)
ax.set_title("Boy's Surface")
plt.show()
