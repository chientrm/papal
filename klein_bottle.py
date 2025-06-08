import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# Force an interactive backend; use 'Qt5Agg' if preferred
matplotlib.use('TkAgg')


def klein_bottle(u, v):
    # Parametric equations for the Klein bottle
    u = np.array(u)
    v = np.array(v)
    x = (np.cos(u) * (np.cos(u / 2) * (np.sqrt(2) + np.cos(v)) +
         np.sin(u / 2) * np.sin(2 * v) / 2))
    y = (np.sin(u) * (np.cos(u / 2) * (np.sqrt(2) + np.cos(v)) +
         np.sin(u / 2) * np.sin(2 * v) / 2))
    z = (-np.sin(u / 2) * (np.sqrt(2) + np.cos(v)) +
         np.cos(u / 2) * np.sin(2 * v) / 2)
    return x, y, z


# Create a grid in parameter space
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
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

# If you see "No module named 'tkinter'", you need to install Tkinter.
# On Ubuntu/Debian, run: sudo apt install python3-tk
# On Fedora: sudo dnf install python3-tkinter
# On Arch: sudo pacman -S tk

# If you cannot install Tkinter, you can try another backend:
# import matplotlib
# matplotlib.use('Qt5Agg')  # Requires PyQt5 or PySide2
