import numpy as np
import scipy
#nb. the words 'mesh' and 'grid' may be used interchangeably, we shall stick with mesh probably
#define extremities of grid 
#generate (mesh) gird

##grid = np.mgrid[0:5,0:5,0:5]

#assign vector to each point in (mesh) grid



#for a given



#Practice

"""
nx, ny, nz = (3,3,3)
x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)
z = np.linspace(0,2,nz)

mesh = np.meshgrid(x,y,z,indexing='xy')
"""

from scipy.interpolate import RegularGridInterpolator
def f(x,y,z):
    return x + y + z

x = np.linspace(1,3,3)
y = np.linspace(1,3,3)
z = np.linspace(1,3,3)

xg, yg, zg = np.meshgrid(x,y,z, indexing='xy')
data = f(xg,yg,zg)



