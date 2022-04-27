import compas
import numpy as np
from compas.geometry import Polyline
from compas_view2.app import App

streamlines = compas.json_load('guiding_str2.json')
#print(streamlines)
N = len(streamlines)
span = [0, N] #range of streamlines that will be printed


def unit_length(streamlines, length): #Divide polylines into unit-long segments
    str_unified = streamlines
    counter = 0
    for i, streamline in enumerate(streamlines[0:120]):
        str_unified[i] = Polyline(streamline.divide_by_length(length, strict=False))
        counter += len(str_unified[i])

    return str_unified, counter


def plotter(vectors, positions, span):
    viewer = App()
    for i in range(span[0], span[1]):
        viewer.add(vectors[i], position=positions[i])
    viewer.show()


def poly_to_vectors(str_unified):   #Converts a polyline into a set of vectors tangential to that polyline
    str_vectors = []
    str_locations = []
    loc = []
    vec = []
    for k, polyline in enumerate(str_unified):
        points = polyline.points
        single_loc = []
        single_vec = []
        #print(points)

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
            str_locations.append([x1, y1, z1])
            str_vectors.append(vector)

        # single_vec = np.gradient(single_loc)
        # single_vec = single_vec / np.linalg.norm(single_vec)


    #print(np.asarray(str_vectors))

        # for point in points:
        #     if point.on_polyline(polyline):
        #         vector = polyline.tangent_at(point)
        #         str_vectors.append(vector)
        #     else:
        #         str_vectors.append(str_vectors[-1])
    return str_vectors, str_locations


str_unified, counter = unit_length(streamlines, 1)


vectors, locations = poly_to_vectors(str_unified)
#print(len(vectors), len(locations))
# vectors = np.array(vectors)
# locations = np.array(locations)
# compas.json_dump(vectors.tolist(), 'guiding_vec2.json')
# compas.json_dump(locations.tolist(), 'guiding_loc2.json')

#plotter(vectors, locations, span)
