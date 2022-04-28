import numpy as np
import pyvista as pv

#be able to store in and append any number of points at a time (where a point is defined as (x,y,z)) to, a numpy array of dimension (N,3) which holds the occupied points



#Check distance between a chosen point and occupied points and return true if distance is cleared
def proximity_check(point, occupied_points, dsep):
    #'occupied_points' is a 2-dimensional array and must be converted to a pyvista pointset
    occupied_points = pv.PointSet(occupied_points)
    index = occupied_points.find_closest_point(point, n = 1)
    distance = np.linalg.norm(occupied_points.points[index]-point)
    return distance >= dsep

output = proximity_check((1,1,1), np.array([[1,1,1],[1,1,1]]), 2)

    
