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

lower_bound = 1
middle_bound = 2
higher_bound = 5
lower_weight = 15
middle_weight = 5
higher_weight = 1
lower_weight /= (lower_weight**2+middle_weight**2+higher_weight**2)**0.5
middle_weight /= (lower_weight**2+middle_weight**2+higher_weight**2)**0.5
higher_weight /= (lower_weight**2+middle_weight**2+higher_weight**2)**0.5

weighted_list = np.zeros(len(idx_short))
for i in idx_short:
    weighted_list[i] = (lower_weight*np.count_nonzero(dd[np.where(idx==i)] <= lower_bound)
      + middle_weight*(np.count_nonzero(dd[np.where(idx==i)] <= middle_bound)-np.count_nonzero(dd[np.where(idx==i)] <= lower_bound))
      + higher_weight*(np.count_nonzero(dd[np.where(idx==i)] <= higher_bound)-np.count_nonzero(dd[np.where(idx==i)] <= middle_bound)))

sorted_weighted = np.argsort(weighted_list)
print(weighted_list[sorted_weighted])
# plt.plot(weighted_list[sorted_weighted])
# plt.show()
plotter = pv.Plotter()

surf = cloud.delaunay_2d(alpha=4.0)
# surf.plot(cpos="xy", show_edges=True)
minimum = 0
for i in idx_short:
    if weighted_list[i] > minimum:
        OldRange = (weighted_list[sorted_weighted][-1] - minimum)
        NewRange = (255 - 0)
        NewValue = (((weighted_list[i] - minimum) * NewRange) / OldRange)
        color = [int(NewValue),255-int(NewValue),0]
        # _ = plotter.add_mesh(points_xyz[np.where(idx == sorted_weighted[i])], color=color)
        spline = pv.Spline(points_xyz[np.where(idx == sorted_weighted[i])], 400)
        _ = plotter.add_mesh(spline, color=color, line_width=5)

_ = plotter.add_mesh(surf)
plotter.show()


# selected_str = []
#
# for i in sorted_idx[0:300]:
#
#     selected_str = np.append(selected_str, points_xyz[np.where(idx == i)])
#