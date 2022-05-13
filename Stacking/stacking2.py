import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt


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

    # find surface