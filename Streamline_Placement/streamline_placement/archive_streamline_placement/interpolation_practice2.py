import numpy as np
from scipy import interpolate

with open("vector_field3D.csv") as f:
    array = np.loadtxt(f,delimiter=",")

print(array)


#creating the vectors at each point
u = array[:,0]
v = array[:,1]
w = array[:,2]

x = np.arange(0,2,1)
y = np.arange(0,2,1)
z = np.arange(0,2,1)

mesh = np.vstack(np.meshgrid(x,y,z)).reshape(3,-1).T

interp_u = interpolate.griddata(mesh, u, (0.5,0.5,0.5), method='linear')
interp_v = interpolate.griddata(mesh, v, (0.5,0.5,0.5), method='linear')

"""
points = (x,y,z)

X, Y, Z = np.meshgrid(x,y,z)

point = np.array([0.5,0.5,0.5])

point_u = interpolate.interpn(points, u, point)
"""      
