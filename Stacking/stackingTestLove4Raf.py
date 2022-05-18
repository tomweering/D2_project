import numpy as np
import pyvista as pv
import scipy.spatial as spatial
import matplotlib.pyplot as plt
# from stacking2 import points
# from stacking2 import streamlines_points, points_xyz
points = np.load('surface_numpypoints.npy')
points_xyz = np.load('streamlines_numpypoints.npy')
idx = np.load('streamlines_index.npy')
idx = idx.astype('int32')

# surf = cloud.delaunay_2d(alpha=1.0)
# surf.plot(cpos="xy", show_edges=True)


cloud = pv.PolyData(points)
#cloud2.plot(point_size=10)
# surf = cloud.delaunay_2d(alpha=4.0)
# surf.plot(cpos="xy", show_edges=True)

tree = spatial.KDTree(points)
dd, ii = tree.query(points_xyz, workers=-1)
# print(len(points))
# print(len(points_xyz))

idx_short = np.arange(idx[-1])

mean = np.zeros(len(idx_short))

for i in idx_short:
    mean[i] = np.mean(dd[np.where(idx == i)])

sorted_idx = idx_short[mean.argsort()]

selected_str = []

for i in sorted_idx[0:50]:

    selected_str = np.append(selected_str, points_xyz[np.where(idx == i)])


print(selected_str)
# selected_cloud = pv.PolyData(selected_str)
# selected_cloud.plot(point_size=10)

