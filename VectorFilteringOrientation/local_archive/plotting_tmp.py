import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x, a, n):
    return a / (a + np.exp(n * x))


Nx = 10
Ny = 10
Nz = 10
linex, liney, linez = (np.linspace(-1, 1, Nx),
                   np.linspace(-1, 1, Ny),
                   np.linspace(-1, 1, Nz))

grid = np.meshgrid(linex,
                   liney,
                   linez)
x, y, z = grid

x_vec = [1]
y_vec = [1]
z_vec = [1]

x_loc = [0.5]
y_loc = [0.5]
z_loc = [0.5]


dist_x = np.abs(x - x_loc * np.ones(np.shape(x)))
dist_y = np.abs(y - y_loc * np.ones(np.shape(x)))
dist_z = np.abs(z - z_loc * np.ones(np.shape(x)))
len = np.sqrt(np.square(dist_x) + np.square(dist_y) + np.square(dist_z))
#coef_matrix = 1 / np.power(10 * (np.sqrt(np.square(dist_x) + np.square(dist_y) + np.square(dist_z)) + 0.0001), 1.5)
a = 10
n = 5
coef_matrix = sigmoid(len, a, n)
value_x = np.ones(np.shape(x)) * coef_matrix
value_y = np.ones(np.shape(x)) * coef_matrix
value_z = np.ones(np.shape(x)) * coef_matrix

print(np.shape(value_x))

fig = plt.figure(dpi=300)
ax = fig.gca(projection='3d')
ax.quiver(x, y, z, value_x, value_y, value_z)
plt.show()