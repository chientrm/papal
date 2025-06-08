import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


def klein_bottle(u, v):
    # Parametric equations for the classic Klein bottle (as in Raylib and Wikipedia)
    x = ((2 + np.cos(u/2) * np.sin(v) - np.sin(u/2) * np.sin(2*v)) * np.cos(u))
    y = ((2 + np.cos(u/2) * np.sin(v) - np.sin(u/2) * np.sin(2*v)) * np.sin(u))
    z = (np.sin(u/2) * np.sin(v) + np.cos(u/2) * np.sin(2*v))
    return x, y, z


# Create a grid in parameter space
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, 2 * np.pi, 40)
u, v = np.meshgrid(u, v)

x, y, z = klein_bottle(u, v)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k',
                linewidth=0.2, alpha=0.9)

ax.set_title("Klein Bottle")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.tight_layout()
plt.show(block=True)  # Ensure the window stays open in some environments
