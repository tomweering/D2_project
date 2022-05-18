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
#print(idx)

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

idx_short = np.arange(idx[-1] + 1)

mean = np.zeros(len(idx_short))

for i in idx_short:
    mean[i] = np.mean(dd[np.where(idx == i)])

sorted_idx = idx_short[mean.argsort()]
print(sorted_idx[0:10])
# selected_short_idx = sorted_idx[0:10]

#selected_long_idx = np.in1d(idx, selected_short_idx)
#selected_str = points_xyz[np.where(np.in1d(idx, selected_short_idx) == True)]

selected_str = []
for i in sorted_idx[0:600]:
#for i in [715, 1515,  666, 1545,  348, 1771, 1713, 1423, 1915, 1894]:
    #print(i)
    #print(np.where(idx == i))
    selected_str = np.append(selected_str, points_xyz[np.where(idx == i)])

selected_cloud = pv.PolyData(selected_str)
selected_cloud.plot(point_size=10)




# print(dd)
# print(ii)
# print(len(dd), len(ii))

# closest_points = points_xyz[ii]
# cloud_close = pv.PolyData(closest_points)
# cloud_close.plot(point_size=5)

# p = pv.Plotter()
# p.add_mesh(h0, smooth_shading=True)
# p.show_grid()
# p.show()

# fig = plt.figure(figsize=(10, 10))
# ax = fig.gca(projection='3d')
# ax.scatter(points[:, 0], points[:, 1], c=points[:, 2])
#
# plt.show()
