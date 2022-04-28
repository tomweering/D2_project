import numpy as np
import matplotlib.pyplot as plt

s = "Streamlines_LowResolution.csv"

int_time = np.genfromtxt(s, skip_header=1, usecols=[3], delimiter=',')
# pointX = np.genfromtxt(s, usecols=[12])
# pointY = np.genfromtxt(s, usecols=[13])
# pointZ = np.genfromtxt(s, usecols=[14])

points_xyz = np.transpose(np.genfromtxt(s, skip_header=1, usecols=(12, 13, 14), delimiter=','))

clear_x = points_xyz[0][np.where(int_time != 0)]
clear_y = points_xyz[1][np.where(int_time != 0)]
clear_z = points_xyz[2][np.where(int_time != 0)]

print(len(clear_x))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(clear_x, clear_y, clear_z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
time_nonzero = int_time[np.where(int_time != 0)]
#print(time_nonzero)

# threshold = 3.0
# print(np.min(abs(np.diff(time_nonzero))))
# plt.plot(np.diff(time_nonzero))
plt.show()

