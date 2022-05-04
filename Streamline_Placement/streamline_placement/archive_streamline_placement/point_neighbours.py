import numpy as np
import pyvista as pv

#number of streamlines to be generated
n = 4

Radius = 0.25

v = np.array([1,1,1])

p = np.array([2.5,2.5,2.5])

v = v/np.linalg.norm(v)
e = np.array([0,0,0])
e[np.argmin(np.abs(v))] = 1

v1 = np.cross(e,v)
v1 = v1/np.linalg.norm(v1)

v2 = np.cross(v,v1)

theta0 = np.arctan(-v1[2]/v2[2])
#define new base points around the chosen base point
#with arange
angles = np.arange(theta0, theta0+(2*np.pi), (2*np.pi)/n)
#with linspace
angles = np.linspace(theta0,theta0+(2*np.pi), 4, endpoint=False)


points = np.array([p]*n) + Radius*(np.cos(angles).reshape((n,1))*(v1*n) + np.sin(angles).reshape((n,1))*(v2*n))

#find angle theta such that change in height (z coordinate is 0):
#2.5 = 2.5 + Radius*(np.cos(theta)*v1 + np.sin(theta)*v2)
#0 = Radius*(np.cos(theta)*v1 + np.sin(theta)*v2)
#therefore: np.cos(theta)*v1[2] = -np.sin(theta)*v2[2]
#therefore: theta = arctan(-v1[2]/v2[2])
#so:



