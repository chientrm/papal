import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)
w = np.linspace(-0.5, 0.5, 20)
theta, w = np.meshgrid(theta, w)

# Parametric equations
x = (1 + w * np.cos(theta / 2)) * np.cos(theta)
y = (1 + w * np.cos(theta / 2)) * np.sin(theta)
z = w * np.sin(theta / 2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='coolwarm', edgecolor='k', linewidth=0.1)
ax.set_title("Mobius Strip")
plt.show()
