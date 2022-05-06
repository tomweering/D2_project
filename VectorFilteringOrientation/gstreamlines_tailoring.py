import compas
import numpy as np
from compas.geometry import Polyline
import matplotlib.pyplot as plt

streamlines = compas.json_load('guiding_str2.json')
N = len(streamlines)
span = [0, N] #range of streamlines that will be printed


def unit_length(streamlines, length): #Divide polylines into unit-long segments
    str_unified = streamlines
    counter = 0
    for i, streamline in enumerate(streamlines[0:120]):
        str_unified[i] = Polyline(streamline.divide_by_length(length, strict=False))
        counter += len(str_unified[i])

    return str_unified, counter

def poly_to_vectors(str_unified):   #Converts a polyline into a set of vectors tangential to that polyline
    str_vectorsx = []
    str_vectorsy = []
    str_vectorsz = []
    str_locationsx = []
    str_locationsy = []
    str_locationsz = []

    for k, polyline in enumerate(str_unified):
        points = polyline.points
        single_loc = []
        single_vec = []

        for i in range(len(points) - 1):
            x1 = points[i].x
            y1 = points[i].y
            z1 = points[i].z

            x2 = points[i + 1].x
            y2 = points[i + 1].y
            z2 = points[i + 1].z

            vector = [x2 - x1,
                      y2 - y1,
                      z2 - z1]
            vector = vector / np.linalg.norm(vector)
            single_loc.append([x1, y1, z1])
            single_vec.append(vector)
        single_vec_coord = np.reshape(np.array(single_vec).T, (3, len(single_vec)))
        single_loc_coord = np.reshape(np.array(single_loc).T, (3, len(single_loc)))

        str_vectorsx.append(single_vec_coord[0])
        str_vectorsy.append(single_vec_coord[1])
        str_vectorsz.append(single_vec_coord[2])
        str_locationsx.append(single_loc_coord[0])
        str_locationsy.append(single_loc_coord[1])
        str_locationsz.append(single_loc_coord[2])


    str_locations = [str_locationsx, str_locationsy, str_locationsz]
    str_vectors = [str_vectorsx, str_vectorsy, str_vectorsz]
    return str_vectors, str_locations

str_unified, counter = unit_length(streamlines, 1)

str_vectors, str_locations = poly_to_vectors(str_unified)

fig = plt.figure(dpi=100)
ax = fig.add_subplot(projection='3d')
for i in range(len(str_vectors[0])):

    locations_x = str_locations[0][i]
    locations_y = str_locations[1][i]
    locations_z = str_locations[2][i]

    vectors_x = str_vectors[0][i]
    vectors_y = str_vectors[1][i]
    vectors_z = str_vectors[2][i]

    ax.scatter(locations_x[::2], locations_y[::2], locations_z[::2])
    #ax.annotate(i, (locations_x[::10], locations_y[::10], locations_z[::10]))
    ax.text(locations_x[0], locations_y[0], locations_z[0], '%s' % (str(i)))
    ax.quiver(locations_x[::10], locations_y[::10], locations_z[::10], vectors_x[::10], vectors_y[::10], vectors_z[::10], length = 6.0)
#plt.legend()
plt.show()
