import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

x = [0,1]
y = [0,1]
z = [0,1]
u = [1,1,1,1,1,1,1,1]
v = [1,1,1,1,1,1,1,1]
w = [1,1,1,1,1,1,1,1]

plt.figure(1)
plt.quiver(x, y, z, u, v, w)
"""
xx = np.linspace(0, 2, 10)
yy = np.linspace(1, 2, 10)
xx, yy = np.meshgrid(xx, yy)

points = np.transpose(np.vstack((x, y)))
u_interp = interpolate.griddata(points, u, (xx, yy), method='cubic')
v_interp = interpolate.griddata(points, v, (xx, yy), method='cubic')

plt.figure(2)
plt.quiver(xx, yy, u_interp, v_interp)
plt.show()
"""
