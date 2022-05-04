import pyvista as pv
import numpy as np
import vtk

# offset array.  Identifies the start of each cell in the cells array
offset = np.array([0, 9])

# Contains information on the points composing each cell.
# Each cell begins with the number of points in the cell and then the points
# composing the cell
cells = np.array([8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15])

# cell type array. Contains the cell type of each cell
cell_type = np.array([vtk.VTK_HEXAHEDRON, vtk.VTK_HEXAHEDRON])

# in this example, each cell uses separate points
cell1 = np.array(
    [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
    ]
)

cell2 = np.array(
    [
        [0, 0, 2],
        [1, 0, 2],
        [1, 1, 2],
        [0, 1, 2],
        [0, 0, 3],
        [1, 0, 3],
        [1, 1, 3],
        [0, 1, 3],
    ]
)

# points of the cell array
points = np.vstack((cell1, cell2))

# create the unstructured grid directly from the numpy arrays
# The offset is optional and will be either calculated if not given (VTK version < 9),
# or is not necessary anymore (VTK version >= 9)
grid = pv.UnstructuredGrid(offset, cells, cell_type, points)

# For cells of fixed sizes (like the mentioned Hexahedra), it is also possible to use the
# simplified dictionary interface. This automatically calculates the cell array with types
# and offsets. Note that for mixing with additional cell types, just the appropriate key needs to be
# added to the dictionary.
cells_hex = np.arange(16).reshape([2, 8])
# = np.array([[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]])
grid = pv.UnstructuredGrid({vtk.VTK_HEXAHEDRON: cells_hex}, points)

# plot the grid (and suppress the camera position output)
_ = grid.plot(show_edges=True)
