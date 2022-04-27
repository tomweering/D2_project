import numpy as np
import matplotlib.pyplot as plt

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

#print(np.shape(x))

# guiding_vectors = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
# print(guiding_vectors)
#
# print(np.reshape(guiding_vectors.T, (3,len(guiding_vectors))))

guiding_vectors = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])
guiding_positions = np.array([[0, 0, 0],
                              [0.5, 0.5, 0.5],
                              [1, 1, 1]])
guiding_vectors_x = np.reshape(guiding_vectors.T, (3,len(guiding_vectors)))[0]
guiding_vectors_y = np.reshape(guiding_vectors.T, (3,len(guiding_vectors)))[1]
guiding_vectors_z = np.reshape(guiding_vectors.T, (3,len(guiding_vectors)))[2]

guiding_positions_coord = np.reshape(guiding_positions.T, (3,len(guiding_positions)))

print(guiding_positions_coord)
guiding = np.zeros(np.shape(grid))

u, v, w = guiding

dist_x = np.abs(x - guiding_positions_coord[0][2] * np.ones(np.shape(grid)))
dist_y = np.abs(y - guiding_positions_coord[1][2] * np.ones(np.shape(grid)))
dist_z = np.abs(z - guiding_positions_coord[2][2] * np.ones(np.shape(grid)))

coef_matrix = 1 / np.power((np.sqrt(np.square(dist_x) + np.square(dist_y) + np.square(dist_z)) + 0.0001), 1.5)

value_matrix_x = guiding_vectors_x[2] * coef_matrix
value_matrix_y = guiding_vectors_y[2] * coef_matrix
value_matrix_z = guiding_vectors_z[2] * coef_matrix



#print(np.abs(x - guiding_positions_coord[0][2] * np.ones(np.shape(grid))))

fig = plt.figure(dpi=300)
ax = fig.gca(projection='3d')
ax.quiver(x, y, z, value_matrix_x, value_matrix_y, value_matrix_z)
plt.show()