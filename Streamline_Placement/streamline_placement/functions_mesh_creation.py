import numpy as np
import pyvista as pv

def mesh_creation(nx, ny, nz, datafile):
    mesh = pv.UniformGrid(dims=(nx, ny, nz), spacing=(1, 1, 1), origin=(0, 0, 0))
    with open(datafile) as f:
        vectors = np.loadtxt(f, delimiter=",")
    ulist, vlist, wlist = vectors[:,0], vectors[:,1], vectors[:,2] #this is incorrect since the vector field he is ordered in x minor, z major order (as required for PyVista) but the scipy ínterpolate method requires x major, z minor ordering!
    mesh['vectors'] = vectors
    return ulist, vlist, wlist, mesh