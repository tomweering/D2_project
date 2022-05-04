import numpy as np
import scipy
#import vtk
import csv
import pyvista as pv
from pyvista import examples


field_ones = np.ones((1000,3))

"""
vtkStreamTracer generates polylines as output. Each cell (polyline) corresponds
to one streamline. Values associated with each streamline are stores in cell
data whereas values associated with points are stored in point data.

Understand the data types 'cell' and 'point' 
"""
#Generating a pyvista uniform grid, since this is what pyvist works with, rather than a numpy array
"""
mesh10_3 = pv.UniformGrid(
    dims=(10,10,10),
    spacing=(1,1,1),
    origin=(0,0,0)
    )

mesh10_3['vectors'] = field_ones


#mesh10_3 = np.vstack(np.meshgrid(np.arange(10),np.arange(10),np.arange(10))).reshape(3,-1).T





#Create a a base streamline in a symple field and mesh


#Example, using PyVista to plot blood flow:

mesh = examples.download_carotid()



streamlines, src = mesh.streamlines(
    return_source=True,
    max_time=100.0,
    initial_step_length=2.0,
    terminal_speed=0.1,
    n_points=1,
    source_radius=2.0,
    source_center=(133.1, 116.3, 5.0),
)

p = pv.Plotter()
p.add_mesh(mesh.outline(), color="k")
p.add_mesh(streamlines.tube(radius=0.15))
p.add_mesh(src)
p.add_mesh(mesh.contour([160]).extract_all_edges(), color="grey", opacity=0.25)
p.camera_position = [(182.0, 177.0, 50), (139, 105, 19), (-0.2, -0.2, 1)]
p.show()


#Applying above example for example vector field of ones on 10x10x10 grid
#testing with simple 10x10x10 grid




mesh = mesh10_3

streamlines, src = mesh.streamlines(
    'vectors',
    return_source=True,
    max_time=100.0,
    initial_step_length = 0.5,
    terminal_speed=100000,
    n_points=1,
    source_radius=2.0,
    source_center=(5,5,5),
)


p = pv.Plotter()
p.add_mesh(mesh.outline(), color="k")
p.add_mesh(streamlines.tube(radius=0.15))
p.add_mesh(src)
p.add_mesh(mesh.contour([160]).extract_all_edges(), color="grey", opacity=0.25)
p.camera_position = [(182.0, 177.0, 50), (139, 105, 19), (-0.2, -0.2, 1)]
p.show()

streamlines.tube().plot()


nx = 20
ny = 15
nz = 5

origin = (-(nx - 1) * 0.1 / 2, -(ny - 1) * 0.1 / 2, -(nz - 1) * 0.1 / 2)
mesh = pv.UniformGrid(dims=(nx, ny, nz), spacing=(0.1, 0.1, 0.1), origin=origin)
x = mesh.points[:, 0]
y = mesh.points[:, 1]
z = mesh.points[:, 2]
vectors = np.empty((mesh.n_points, 3))
vectors[:, 0] = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
vectors[:, 1] = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
vectors[:, 2] = np.sqrt(3.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z)

mesh['vectors'] = vectors

stream, src = mesh.streamlines(
    'vectors', return_source=True, terminal_speed=0.0, n_points=200, source_radius=0.1
)

cpos = [(1.2, 1.2, 1.2), (-0.0, -0.0, -0.0), (0.0, 0.0, 1.0)]
stream.tube(radius=0.0015).plot(cpos=cpos)

"""

nx = 10
ny = 10
nz = 10

origin = (0,0,0)
mesh10_3 = pv.UniformGrid(dims=(nx,ny,nz), spacing=(1,1,1), origin=origin)
x = mesh10_3.points[:,0]
y = mesh10_3.points[:,1]
z = mesh10_3.points[:,2]
vectors = np.empty((mesh10_3.n_points,3))
vectors[:,0] = np.ones(mesh10_3.n_points)
vectors[:,1] = np.ones(mesh10_3.n_points)
vectors[:,2] = np.ones(mesh10_3.n_points)

mesh10_3['vectors'] = vectors

stream,src = mesh10_3.streamlines(
    'vectors', return_source=True, terminal_speed=0.0, n_points=5,source_radius=1
    )

p = pv.Plotter()
p.add_mesh(mesh10_3.outline())
p.add_mesh(stream.tube(radius=0.01))
p.add_mesh(src)
p.show()

"""
stream.tube(radius=0.1).plot()
"""
