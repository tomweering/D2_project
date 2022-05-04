import numpy as np
from scipy import interpolate

#arrays constituting the 3D grid
x = np.linspace(0, 50, 50)
y = np.linspace(0, 50, 50)
z = np.linspace(0, 50, 50)
points = (x, y, z)
#generate a 3D grid
X, Y, Z = np.meshgrid(x, y, z)

def func_3d(X,Y,Z):
    return 2*X + 3*Y -Z

#evaluate the function on the points of the grid
values = func_3d(X, Y, Z) 

point = np.array([2.5, 3.5, 1.5])

# points = the regular grid, #values =the data on the regular grid
# point = the point that we want to evaluate in the 3D grid
print(interpolate.interpn(points, values, point))
