import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator


def interp_field(field, coords, shape):
    interpolator = RegularGridInterpolator(
        (gridZ[:, 0, 0], gridY[0, :, 0], gridX[0, 0, :]), field)
    return interpolator(coords).reshape(shape)


gridZ, gridY, gridX = np.mgrid[0:1.5:0.5, 0:1.5:0.5, 0:1.5:0.5]

#get vector data in mesh form from csv file
u = np.sin(np.pi * gridX) * np.cos(np.pi * gridY) * np.cos(np.pi * gridZ)
v = -np.cos(np.pi * gridX) * np.sin(np.pi * gridY) * np.cos(np.pi * gridZ)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * gridX) * np.cos(np.pi * gridY) *
     np.sin(np.pi * gridZ))

interp_gridZ, interp_gridY, interp_gridX = np.mgrid[
    0:1.25:0.25, 0:1.25:0.25, 0:1.25:0.25]
interp_coords = np.column_stack(
    (interp_gridZ.flatten(), interp_gridY.flatten(), interp_gridX.flatten()))
interp_u = interp_field(u, interp_coords, interp_gridX.shape)
interp_v = interp_field(v, interp_coords, interp_gridX.shape)
interp_w = interp_field(w, interp_coords, interp_gridX.shape)

fig, (ax, bx) = plt.subplots(ncols=2, subplot_kw=dict(projection='3d'),
                             constrained_layout=True)
ax.quiver(gridX, gridY, gridZ, u, v, w, length=0.3)
bx.quiver(interp_gridX, interp_gridY, interp_gridZ,
          interp_u, interp_v, interp_w, length=0.3)
plt.show()
