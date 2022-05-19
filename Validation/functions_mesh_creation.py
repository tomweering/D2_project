import numpy as np
import pyvista as pv


def mesh_creation(nx, ny, nz, datafileXmZM, datafileXMZm):
    mesh_pyvista = pv.UniformGrid(dims=(nx, ny, nz), spacing=(1, 1, 1), origin=(0, 0, 0))
    with open(datafileXmZM) as XmZM:
        vectors_pyvista = np.loadtxt(XmZM, delimiter=",")
    mesh_pyvista['vectors'] = vectors_pyvista

    x_list = np.arange(nx)
    y_list = np.arange(ny)
    z_list = np.arange(nz)

    # combine xyz arrays and reformat into np mesh for use with interpolator (which is defined on SciPy)
    mesh_scipy = np.vstack(np.meshgrid(x_list, y_list, z_list)).reshape(3, -1).T
    with open(datafileXMZm) as XMZm:
        vectors_scipy = np.loadtxt(XMZm, delimiter=",")
    u_list, v_list, w_list = vectors_scipy[:, 0], vectors_scipy[:, 1], vectors_scipy[:,2]  # this is incorrect since the vector field he is ordered in x minor, z major order (as required for PyVista) but the scipy ínterpolate method requires x major, z minor ordering!

    return mesh_pyvista, mesh_scipy, u_list, v_list, w_list

def extracted_mesh(mesh_pyvista, bounds):
    #bounds have format: (xmin, xmax, ymin, ymax, zmin, zmax)
    mesh_pyvista_extracted = mesh_pyvista.extract_subset(bounds)
    return mesh_pyvista_extracted

def mesh_adjustment(mesh):
    #make sure all associated w vectors for the parsed mesh are positive (i.e. pointing up)
    mesh['vectors'][:,1] = abs(mesh['vectors'][:,1])
    return mesh
