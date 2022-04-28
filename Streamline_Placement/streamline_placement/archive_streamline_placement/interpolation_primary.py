import numpy as np
from scipy import interpolate


#putting uvw vectors from csv file into array
with open("field_vect_3.csv") as f:
    array = np.loadtxt(f,delimiter=",")

#defining size of coordinate space
x_size,y_size,z_size = (95,59,36)

#coordinates at which we want to interpolate the vector field
x = 30
y = 25
z = 15

method = 'linear'

#sets of vectors in all three directions for all points in mesh
u_list = array[:,0]
v_list = array[:,1]
w_list = array[:,2]


#generating points for mesh generation
x_list = np.arange(x_size)
y_list = np.arange(y_size)
z_list = np.arange(z_size)

#combine xyz arrays and reformat into mesh 
mesh = np.vstack(np.meshgrid(x_list,y_list,z_list)).reshape(3,-1).T

#interpoalting for u,v,w values at a particular xyz coordinate
#u_new = interpolate.griddata(mesh, u_list, (x,y,z), method=method)
#v_new = interpolate.griddata(mesh, v_list, (x,y,z), method=method)
#w_new = interpolate.griddata(mesh, w_list, (x,y,z), method=method)

#defining function for interpolation on a discretely-defined VECTOR FIELD given as LISTS of u, v and w, defined on a MESH. Interpolation done for xyz coordinates using a specified interpolation METHOD (nearest or linear (cubic doesnt work on 3D))
"""------------------------------------------------------------------------------------------"""
def interpolator(mesh, u_list, v_list, w_list, point, method):
    #input method in function with quote marks
    u_new = interpolate.griddata(mesh, u_list, point, method='nearest')
    v_new = interpolate.griddata(mesh, v_list, point, method='nearest')
    w_new = interpolate.griddata(mesh, w_list, point, method='nearest')
    return np.array([u_new,v_new,w_new])


#vaguely testing the function
#print(interpolator(mesh, u_list, v_list, w_list, x, y, z, method))

x_sample = np.random.uniform(0,x_size,1000)
y_sample = np.random.uniform(0,y_size,1000)
z_sample = np.random.uniform(0,z_size,1000)
"""------------------------------------------------------------------------------------------"""

#defining function that generates the interpolated vector field values at a point. Produces an output that can be parsed by the vector plotting function.

     
