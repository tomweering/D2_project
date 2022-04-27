import numpy as np
import matplotlib.pyplot as plt
import compas
from str_to_gvectors import vectors, locations


def sigmoid(x, a, n, off):
    return (a + 1) / (a + np.exp(n * (x - off)))


# vectors = compas.json_load('guiding_vec2.json')
# locations = compas.json_load('guiding_loc2.json')
vectors = np.array(vectors)
locations = np.array(locations)

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

locations_x = np.reshape(locations.T, (3,len(locations)))[0]
locations_y = np.reshape(locations.T, (3,len(locations)))[1]
locations_z = np.reshape(locations.T, (3,len(locations)))[2]

vectors_x = np.reshape(vectors.T, (3,len(vectors)))[0]
vectors_y = np.reshape(vectors.T, (3,len(vectors)))[1]
vectors_z = np.reshape(vectors.T, (3,len(vectors)))[2]

#print(vectors_z)

# fig = plt.figure(dpi=300)
# ax = fig.gca(projection='3d')
# ax.quiver(locations_x, locations_y, locations_z, vectors_x, vectors_y, vectors_z)
# plt.show()

#print(len(locations_x), locations_x)
N = len(locations_x)
point_xg = np.zeros(N)
point_yg = np.zeros(N)
point_zg = np.zeros(N)

value_x = np.zeros(np.shape(x))
value_y = np.zeros(np.shape(x))
value_z = np.zeros(np.shape(x))

for i in range(0, N, 1):
    point_xg[i] = linex[np.argmin(np.abs(linex - np.ones(np.shape(linex)) * locations_x[i]))]
    point_yg[i] = liney[np.argmin(np.abs(liney - np.ones(np.shape(liney)) * locations_y[i]))]
    point_zg[i] = linez[np.argmin(np.abs(linez - np.ones(np.shape(linez)) * locations_z[i]))]

    #print(point_xg[i])
    dist_x = np.abs(x - point_xg[i] * np.ones(np.shape(x)))
    dist_y = np.abs(y - point_yg[i] * np.ones(np.shape(x)))
    dist_z = np.abs(z - point_zg[i] * np.ones(np.shape(x)))
    distance = np.sqrt(np.square(dist_x) + np.square(dist_y) + np.square(dist_z))

    a = 5
    n = 1.5
    off = 0

    coef_matrix = sigmoid(distance, a, n, off)


    value_x += np.ones(np.shape(x)) * vectors_x[i] * coef_matrix
    value_y += np.ones(np.shape(x)) * vectors_y[i] * coef_matrix
    value_z += np.ones(np.shape(x)) * vectors_z[i] * coef_matrix


# point_xg[0] = linex[np.argmin(np.abs(linex - np.ones(np.shape(linex)) * locations_x[0]))]
# point_yg[0] = liney[np.argmin(np.abs(liney - np.ones(np.shape(liney)) * locations_y[0]))]
# point_zg[0] = linez[np.argmin(np.abs(linez - np.ones(np.shape(linez)) * locations_z[0]))]
#
#
# dist_x = np.abs(x - point_xg[0] * np.ones(np.shape(x)))
# dist_y = np.abs(y - point_yg[0] * np.ones(np.shape(x)))
# dist_z = np.abs(z - point_zg[0] * np.ones(np.shape(x)))
# distance = np.sqrt(np.square(dist_x) + np.square(dist_y) + np.square(dist_z))
#
# a = 10
# n = 2
# off = 10
#
# coef_matrix = sigmoid(distance, a, n, off)
#
# print(coef_matrix)
#
# value_x = np.ones(np.shape(x)) * coef_matrix
# value_y = np.ones(np.shape(x)) * coef_matrix
# value_z = np.ones(np.shape(x)) * coef_matrix


#final_vector = np.array([value_x, value_y, value_z])
#final_normalized = final_vector/ np.linalg.norm(final_vector)

#print(final_vector[0][0], final_vector[1])

guiding_field = [value_x, value_y, value_z]
value_x[np.where(np.abs(value_x) < 0.05)] = 0
value_y[np.where(np.abs(value_y) < 0.05)] = 0
value_z[np.where(np.abs(value_z) < 0.05)] = 0

fig = plt.figure(dpi=300)
ax = fig.gca(projection='3d')
#ax.quiver(locations_x, locations_y, locations_z, vectors_x, vectors_y, vectors_z, color='red')
ax.quiver(x, y, z, value_x, value_y, value_z)
plt.show()

np.save('guiding_field.npy', guiding_field)