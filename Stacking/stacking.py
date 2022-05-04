import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


def getXYZ(s):
    s = "Streamlines_HighResolution.csv"

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

    # iso indexing
    linear = np.linspace(0, len(points_xyz) - 1, len(points_xyz))
    zeros = np.zeros(len(points_xyz))
    mesharr1, mesharr2 = np.meshgrid(linear, zeros)
    iso_index = np.c_[mesharr1.ravel(), mesharr2.ravel()]
    current_index = 1
    statistics = np.zeros((len(points_xyz), 6))
    for i in range(len(points_xyz)):
        points_x, points_y, points_z = points_xyz[i].T
        statistics[i][0] = np.mean(points_x)
        statistics[i][1] = np.std(points_x)
        statistics[i][2] = np.mean(points_y)
        statistics[i][3] = np.std(points_y)
        statistics[i][4] = np.mean(points_z)
        statistics[i][5] = np.std(points_z)

    sortedStreamlines = points_xyz
    inter = np.tile(statistics[0], (len(statistics), 1))
    inter = np.sum((inter - statistics) ** 2, axis=1)
    sortedIndex = inter.argsort()
    statistics = statistics[sortedIndex]
    sortedStreamlines = points_xyz[sortedIndex]

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')

    # for i in range(1,100):
    #     angle = np.rad2deg(np.arctan(abs(statistics[i][4] - statistics[0][4]) / (
    #                 (statistics[i][0] - statistics[0][0]) ** 2 + (statistics[i][2] - statistics[0][2]) ** 2) ** 0.5))
    #     if angle < 10:
    #         x1, y1, z1 = sortedStreamlines[i].T
    #         ax.scatter(x1, y1, z1)
    x = np.linspace(0,len(inter),len(inter))
    inters = inter[sortedIndex]
    plt.plot(x,inters)
    plt.show()
    # plt.show()