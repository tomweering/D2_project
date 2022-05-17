import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.spatial as spatial
import alphashape
from descartes import PolygonPatch


def getXYZ(s):
    s = sys.path[1] + "\\3D_Bracket\Streamlines_HighResolution.csv"

    int_time = np.genfromtxt(s, skip_header=1, usecols=[3], delimiter=',')
    points_xyz = np.transpose(np.genfromtxt(s, skip_header=1, usecols=(12, 13, 14), delimiter=','))

    mask = np.ones(len(int_time))  # has zeros where integration time = 0 and ones where integration time != 0
    mask[np.where(int_time == 0)] = 0

    gradient_mask = np.diff(mask)  # takes a difference a[i+1] - a[i] for all i. Effectively it's a gradient of mask

    mask_start = np.where(gradient_mask > 0.0)  # integration time goes from 0 to smth non-zero: streamline starts
    mask_stop = np.where(gradient_mask < 0.0)  # integration time goes from smth non-zero to 0: streamline stops

    streamlines_x = []
    streamlines_y = []
    streamlines_z = []

    for i in range(len(mask_start[0]) - 1):
        new_x = points_xyz[0][mask_start[0][i]: mask_stop[0][i]]  # start_point:end_point
        new_y = points_xyz[1][mask_start[0][i]: mask_stop[0][i]]
        new_z = points_xyz[2][mask_start[0][i]: mask_stop[0][i]]

        streamlines_x.append(new_x)
        streamlines_y.append(new_y)
        streamlines_z.append(new_z)

    ids = np.zeros(len(streamlines_x))

    streamlines = np.array(
        [np.transpose([streamlines_x[i], streamlines_y[i], streamlines_z[i]]) for i in range(len(streamlines_x))],
        dtype=object)
    return streamlines, ids


# ------------------------MAIN--------------------------#

if __name__ == '__main__':
    # get the streamlines from cvs file
    s = "Streamlines_lowResolution.csv"
    points_xyz, idx = getXYZ(s)
    points_xyz = np.vstack(points_xyz)
    points_xy = np.delete(points_xyz,2,1)

    field_dimensions = [95, 59, 36]
    left_bnd = [-167.186099, -78.232828, -4.077015]
    right_bnd = [19.129499, 37.478964, 66.526791]

    Nx, Ny, Nz = field_dimensions
    linex, liney, linez = (np.linspace(left_bnd[0], right_bnd[0], Nx),
                           np.linspace(left_bnd[1], right_bnd[1], Ny),
                           np.linspace(left_bnd[2], right_bnd[2], Nz))

    point_tree = spatial.cKDTree(points_xy)
    surface = np.array([])
    for x in linex:
        for y in liney:
            potential_points = point_tree.query_ball_point([x, y], 1)
            u,v,w = points_xyz[potential_points].T
            if not w.size == 0:
                surface = np.append(surface, potential_points[np.argmin(w)])
    surface = surface.astype(int)
    print(points_xyz[surface])
    fig = plt.figure()
    ax = fig.add_subplot()
    x1,y1,z1 = points_xyz[surface].T
    points_xy_hull = np.delete(points_xyz[surface],2,1)
    ax.scatter(x1, y1)
    alpha = 0.95 * alphashape.optimizealpha(points_xy_hull)
    hull = alphashape.alphashape(points_xy_hull, alpha)
    hull_pts = hull.exterior.coords.xy
    ax.scatter(hull_pts[0], hull_pts[1], color='red')
    ax.add_patch(PolygonPatch(hull, fill=False, color='green'))
    plt.show()
