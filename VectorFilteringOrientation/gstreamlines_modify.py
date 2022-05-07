import compas
import numpy as np
from compas.geometry import Polyline
import matplotlib.pyplot as plt

streamlines = compas.json_load('guiding_str3.json')
N = len(streamlines)
span = [0, N] #range of streamlines that will be printed

str_to_invert = [35, 19, 17, 18, 41, 14, 13, 15, 12, 11, 8, 9, 16, 10, 39, 28, 29, 27, 26, 25]
str_to_delete = [10, 36]

if_modify = True



def unit_length(streamlines, length): #Divide polylines into unit-long segments
    str_unified = streamlines
    str_unified_points = []

    for i, streamline in enumerate(streamlines[0:120]):
        str_unified[i] = Polyline(streamline.divide_by_length(length, strict=False))
        str_unified_points.append(str_unified[i].points)
        #counter += len(str_unified[i])


    return str_unified, str_unified_points


def modify(invert, delete,  streamlines):
    for i in invert:
        streamlines[i].reverse()
    # for i in delete:
    #     del streamlines[i]
    #del streamlines[delete]
    return streamlines

def poly_to_vectors(str_unified_points):   #Converts a polyline into a set of vectors tangential to that polyline
    str_vectorsx = []
    str_vectorsy = []
    str_vectorsz = []
    str_locationsx = []
    str_locationsy = []
    str_locationsz = []
    vectors = []
    locations = []
    # for k, polyline in enumerate(str_unified):
    #     points = polyline.points
    for k, points in enumerate(str_unified_points):
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
            locations.append([x1, y1, z1])
            vectors.append(vector)
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
    return str_vectors, str_locations, vectors, locations

str_unified, str_points = unit_length(streamlines, 1)

if if_modify:
    str_points = modify(str_to_invert, str_to_delete, str_points)

str_vectors, str_locations, vectors, locations = poly_to_vectors(str_points)

fig = plt.figure(dpi=100)
ax = fig.add_subplot(projection='3d')
plt.axis('off')
plt.grid(b=None)
for i in range(len(str_vectors[0])):

    locations_x = str_locations[0][i]
    locations_y = str_locations[1][i]
    locations_z = str_locations[2][i]

    vectors_x = str_vectors[0][i]
    vectors_y = str_vectors[1][i]
    vectors_z = str_vectors[2][i]

    #ax.scatter(locations_x[::2], locations_y[::2], locations_z[::2])
    #ax.annotate(i, (locations_x[::10], locations_y[::10], locations_z[::10]))
    ax.text(locations_x[0], locations_y[0], locations_z[0], '%s' % (str(i)))
    ax.text(locations_x[-1], locations_y[-1], locations_z[-1], '%s' % (str(i)))
    ax.quiver(locations_x[::10], locations_y[::10], locations_z[::10], vectors_x[::10], vectors_y[::10], vectors_z[::10], length = 6.0)
#plt.legend()
plt.show()
