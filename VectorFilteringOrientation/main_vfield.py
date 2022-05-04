import matplotlib.pyplot as plt
import numpy as np

# If input data has been updated, please first run:
# str_to_gvectors.py ; initial_vectorfield.py ;  gvfield_scattering.py
# You may want to change names of the .npy storage files to retain the old results.

guiding_field = np.load('guiding_field.npy')
vector_grid = np.load('initial_vectorgrid.npy')

vi_x, vi_y, vi_z = vector_grid
vg_x, vg_y, vg_z = guiding_field

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

dot_product = (np.multiply(vi_x, vg_x) + np.multiply(vi_y, vg_y) + np.multiply(vi_z, vg_z))

print(np.shape(dot_product))
print((np.where(dot_product < 0)))

flip = np.where(dot_product < 0.0)
flip_mask = np.ones(np.shape(dot_product))

flip_mask[flip] = -1

vinv_x = np.multiply(vi_x, flip_mask)
vinv_y = np.multiply(vi_y, flip_mask)
vinv_z = np.multiply(vi_z, flip_mask)

# TODO: Make the plotting commands into a function
fig = plt.figure(dpi=300)
ax = fig.gca(projection='3d')
ax.quiver(x, y, z, vi_x, vi_y, vi_z, color='red')
#ax.quiver(x, y, z, vg_x, vg_y, vg_z, color='green')
ax.quiver(x, y, z, vinv_x, vinv_y, vinv_z, color='blue')
plt.show()