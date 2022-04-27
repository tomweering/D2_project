import matplotlib.pyplot as plt
import numpy as np

# That field converts vectors given as a list in file 'field_vect_scaledByDensity.csv'
# to a grid-like 4d numpy array.


field_dimensions = [95, 59, 36]
left_bnd = [-167.186099, -78.232828, -4.077015]
right_bnd = [19.129499, 37.478964, 66.526791]

Nx, Ny, Nz = field_dimensions
linex, liney, linez = (np.linspace(left_bnd[0], right_bnd[0], Nx),
                   np.linspace(left_bnd[1], right_bnd[1], Ny),
                   np.linspace(left_bnd[2], right_bnd[2], Nz))

grid = np.meshgrid(linex,
                   liney,
                   linez)
x, y, z = grid

vectors = np.genfromtxt('field_vect_scaledByDensity.csv', skip_header=10, delimiter=',')

vector_grid = np.zeros(np.shape(grid))

# If somebody knows how to vectorize (using reshape function etc) the code belowe, please implement that
i = 0
for k in range(field_dimensions[0]):
    for l in range(field_dimensions[1]):
        for m in range(field_dimensions[2]):

            if np.linalg.norm(vectors[i]) >= 0.05:  # Remove vectors with module < 0.05
                vector_grid[0][l][k][m] = vectors[i][0]
                vector_grid[1][l][k][m] = vectors[i][1]
                vector_grid[2][l][k][m] = vectors[i][2]

            i += 1


# This example of vectorized method gives incorrect results:
# vector_grid1 = np.reshape(vectors, (3, 201780))
# vec_x1, vec_y1, vec_z1 = vector_grid1
# vec_x = np.reshape(vec_x1, (59, 95, 36))
# vec_y = np.reshape(vec_y1, (59, 95, 36))
# vec_z = np.reshape(vec_z1, (59, 95, 36))
# vector_grid = np.reshape(vectors, (3, 95, 59, 36))
# vector_grid = np.reshape(vectors, (3, 59, 95, 36), order='A')
# remove_vectors = np.where((np.abs(vector_grid[0]) + np.abs(vector_grid[1]) + np.abs(vector_grid[2])) < 0.1)
# remove_vectors = np.where(np.linalg.norm([vec_x, vec_y, vec_z]) < 0.1)

vec_x, vec_y, vec_z = vector_grid

np.save('initial_vectorgrid.npy', vector_grid)

#Uncomment to plot:
# fig = plt.figure(dpi=300)
# ax = fig.gca(projection='3d')
# ax.quiver(x, y, z, vec_x, vec_y, vec_z)
# plt.show()