import numpy as np
import pyvista as pv

from interpolation_primary import interpolator, mesh, u_list, v_list, w_list

field_ones = np.ones((1000,3))
#stream.tube(radius=0.1).plot()

#Streamline generation with streamlines_from_source
nx = 10
ny = 10
nz = 10

seed_points = [(5.,5.,0.),(0.,0.,0.),(4,2,8)]
mesh10_3 = pv.UniformGrid(dims=(nx,ny,nz), spacing=(1,1,1), origin=(0,0,0))


x_size,y_size,z_size = (10,10,10)

#generating points for mesh generation
x_list = np.arange(x_size)
y_list = np.arange(y_size)
z_list = np.arange(z_size)

#combine xyz arrays and reformat into mesh
mesh10_3np = np.vstack(np.meshgrid(x_list,y_list,z_list)).reshape(3,-1).T

x = mesh10_3.points[:,0]
y = mesh10_3.points[:,1]
z = mesh10_3.points[:,2]
vectors = np.empty((mesh10_3.n_points,3))
vectors[:,0] = np.ones(mesh10_3.n_points)
vectors[:,1] = np.ones(mesh10_3.n_points)
vectors[:,2] = np.ones(mesh10_3.n_points)

mesh10_3['vectors'] = vectors

u_list,v_list,w_list = vectors[:,0],vectors[:,1],vectors[:,2]