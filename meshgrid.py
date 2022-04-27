import numpy as np
import matplotlib.pyplot as plt

Nx = 10
Ny = 10
Nz = 10

grid = np.meshgrid(np.linspace(-1, 1, Nx),
                   np.linspace(-1, 1, Ny),
                   np.linspace(-1, 1, Nz))
x, y, z = grid

aim_vector = ()

# u = np.random.random_integers(-1, 1) * np.random.random()
# v = np.random.random()
# w = np.random.random_integers(-1, 1) * np.random.random()

# values = np.random.random(np.shape(grid))
# u, v, w = values

u = np.sin(3 * x)
v = np.cos(2 * y)
w = 1

fig = plt.figure(dpi=300)
ax = fig.gca(projection='3d')
ax.quiver(x, y, z, u, v, w, length=0.1)
plt.show()