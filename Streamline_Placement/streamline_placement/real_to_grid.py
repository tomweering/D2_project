import numpy as np

#This function projects a list of point-coordinates in real-body coordinate frame into grid coordinates

field_dimensions = [95, 59, 36]
left_bnd = [-167.186099, -78.232828, -4.077015]
right_bnd = [19.129499, 37.478964, 66.526791]

Nx, Ny, Nz = field_dimensions
linex, liney, linez = (np.linspace(left_bnd[0], right_bnd[0], Nx),
                   np.linspace(left_bnd[1], right_bnd[1], Ny),
                   np.linspace(left_bnd[2], right_bnd[2], Nz))

def to_grid_coord(coordinates):
    coordinates_grid = np.ones(np.shape(coordinates))
    for i in range(len(coordinates)):
        coordinates_grid[i][0] = np.argmin(np.abs(linex - np.ones(np.shape(linex)) * coordinates[i][0]))
        coordinates_grid[i][1] = np.argmin(np.abs(liney - np.ones(np.shape(liney)) * coordinates[i][1]))
        coordinates_grid[i][2] = np.argmin(np.abs(linez - np.ones(np.shape(linez)) * coordinates[i][2]))

    print(coordinates_grid)
    return coordinates_grid

coordinates = [[-30, -7.5, 20]]

to_grid_coord(coordinates)