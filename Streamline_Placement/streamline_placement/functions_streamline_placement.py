import numpy as np
import pyvista as pv
from scipy import interpolate
#from inputs_streamline_placement import *


def streamline(mesh, seed_point, integration_direction, initial_step_length, step_unit, min_step_length, max_steps,
               terminal_speed):
    return mesh.streamlines_from_source(seed_point, vectors="vectors", integrator_type=45,
                                        integration_direction=integration_direction,
                                        initial_step_length=initial_step_length, step_unit=step_unit,
                                        min_step_length=min_step_length, max_steps=max_steps,
                                        terminal_speed=terminal_speed)


# Check distance between a chosen point and occupied points and return true if distance is cleared
def proximity_check(point, occupied_points, dsep):
    # 'occupied_points' is a 2-dimensional array and must be converted to a pyvista pointset
    occupied_points = pv.PointSet(occupied_points)
    index = occupied_points.find_closest_point(point, n=1)
    distance = np.linalg.norm(occupied_points.points[index] - point)
    #print("distance",distance,"twice dsep", 2*dsep)
    return (distance >= 3*dsep)


def lines_from_points(points):
    """Create a line based on an array of points"""
    poly = pv.PolyData()
    poly.points = points
    cells = np.full((len(points) - 1, 3), 2, dtype=np.int_)
    cells[:, 1] = np.arange(0, len(points) - 1, dtype=np.int_)
    cells[:, 2] = np.arange(1, len(points), dtype=np.int_)
    poly.lines = cells
    return poly


def interpolator(mesh, u_list, v_list, w_list, point, method):
    # input method in function with quote marks
    u_new = float(interpolate.griddata(mesh, u_list, point, method=method))
    v_new = float(interpolate.griddata(mesh, v_list, point, method=method))
    w_new = float(interpolate.griddata(mesh, w_list, point, method=method))
    return np.array([u_new, v_new, w_new])

def interpolator2(mesh_pyvista, point):
    closest_point_index = mesh_pyvista.find_closest_point(point, n=1)
    #closest_point = mesh_pyvista.point[closest_point_index]
    #print("closest point",mesh_pyvista.points[closest_point_index])
    closest_defined_vector = mesh_pyvista["vectors"][closest_point_index]
    return closest_defined_vector

def new_seed_points(n_seed_points, dsep, point, mesh_pyvista, mesh_scipy, u_list, v_list, w_list):
    """ for a given point on a given streamline, find possible new seed points """
    n = n_seed_points
    base_vector = interpolator(mesh_scipy, u_list, v_list, w_list, point, "nearest")

    base_vector = interpolator2(mesh_pyvista, point)
    #print(base_vector)
    base_vector = base_vector / np.linalg.norm(base_vector)
    e = np.array([0, 0, 0])
    e[np.argmin(np.abs(base_vector))] = 1

    v1 = np.cross(e, base_vector)
    v1 = v1 / np.linalg.norm(v1)

    v2 = np.cross(base_vector, v1)
    #print(base_vector)
    #print(v1)
    #print(v2)
    theta0 = np.arctan(-v1[2] / v2[2])
    #print(theta0)
    # define new base points around the chosen base point
    angles = np.arange(theta0, theta0 + (2 * np.pi), (2 * np.pi) / n)
    # define new points
    points = np.array([point]*4) + (dsep) * (np.cos(angles).reshape((n, 1)) * (v1 * n) + np.sin(angles).reshape((n, 1)) * (v2 * n))
    """Description"""
    # find angle theta such that change in height (z coordinate is 0):
    # 2.5 = 2.5 + Radius*(np.cos(theta)*v1 + np.sin(theta)*v2)
    # 0 = Radius*(np.cos(theta)*v1 + np.sin(theta)*v2)
    # therefore: np.cos(theta)*v1[2] = -np.sin(theta)*v2[2]
    # therefore: theta = arctan(-v1[2]/v2[2])
    return points


def seed_point_filter(points, occupied_points, dsep, mesh):
    filter_array = []
    # if the element is closer than dsep to any occupied point, its index in the filter array is set to False
    for i in points:
        print("proximity",proximity_check(i,occupied_points,dsep), "boundary", boundary_check(mesh,i))
        if proximity_check(i, occupied_points, dsep) and np.linalg.norm(interpolator2(mesh, i)) > 0.75:
            filter_array.append(True)
        else:
            filter_array.append(False)
    return points[filter_array]

def boundary_check(mesh, point):

    index_closest_point = mesh.find_closest_point(point, n = 1)
    closest_vector = mesh["vectors"][index_closest_point]
    return np.linalg.norm(closest_vector)>0.
