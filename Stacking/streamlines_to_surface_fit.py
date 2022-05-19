import numpy as np
import pyvista as pv
import scipy.spatial as spatial
import matplotlib.pyplot as plt
# from stacking2 import points
# from stacking2 import streamlines_points, points_xyz
surface_points = np.load('surface_numpypoints.npy')
points_xyz = np.load('hr_eq_spaced.npy')
idx = np.load('hr_eq_spaced_idx.npy')
idx = idx.astype('int32')

# surf = cloud.delaunay_2d(alpha=1.0)
# surf.plot(cpos="xy", show_edges=True)

def lines_from_points(points):
    """Given an array of points, make a line set"""
    poly = pv.PolyData()
    poly.points = points
    cells = np.full((len(points) - 1, 3), 2, dtype=np.int_)
    cells[:, 1] = np.arange(0, len(points) - 1, dtype=np.int_)
    cells[:, 2] = np.arange(1, len(points), dtype=np.int_)
    poly.lines = cells
    return poly

cloud = pv.PolyData(surface_points)
#cloud2.plot(point_size=10)
surf = cloud.delaunay_2d(alpha=4.0)
# surf.plot(cpos="xy", show_edges=True)

tree = spatial.KDTree(surface_points)
dd, ii = tree.query(points_xyz, workers=-1)
# print(len(points))
# print(len(points_xyz))

idx_short = np.arange(idx[-1])

mean = np.zeros(len(idx_short))

for i in idx_short:
    mean[i] = np.mean(dd[np.where(idx == i)])

sorted_idx = idx_short[mean.argsort()]

# selected_short_idx = sorted_idx[0:10]

#selected_long_idx = np.in1d(idx, selected_short_idx)
#selected_str = points_xyz[np.where(np.in1d(idx, selected_short_idx) == True)]

p = pv.Plotter()
selected_str = []
print(sorted_idx)
for i in sorted_idx[0:800]:
    streamline_local = points_xyz[np.where(idx == i)]
    selected_str = np.append(selected_str, streamline_local)
    line = lines_from_points(streamline_local)
    line["scalars"] = dd[np.where(idx == i)]
    tube = line.tube(radius=0.1)
    p.add_mesh(tube, show_edges=False)
p.add_mesh(surf)
# for i in range(500):
#     line = lines_from_points(points_xyz[np.where(idx == i)])
#     line["scalars"] = np.arange(line.n_points)
#     tube = line.tube(radius=0.1)
#     p.add_mesh(tube, color="tan", show_edges=True)
# selected_cloud = pv.PolyData(selected_str)
# selected_cloud.plot(point_size=10)

p.show()