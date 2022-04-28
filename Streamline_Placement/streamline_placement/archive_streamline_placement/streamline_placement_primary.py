import numpy as np
import scipy
#import vtk
import csv
import pyvista as pv
from streamline_generation_primary import mesh10_3, initial_streamline
from interpolation_primary import interpolator, mesh, u_list, v_list, w_list

#pyvista find vector at point#define separation distance, dsep, between streamlines and the checking parameter to avoid colisions, dtest (a proportional param. between 0 and 1)
dsep = 0.5 #unit lengths
dtest = 1 #proportion parameter

#create queue of streamlines
queue = []

#definition of seed point for frist streamline
#init_point = np.array([[ 8.15685425, -3.15685425,  2.5],[ 5.76598632,  5.76598632, -4.03197265], [-3.15685425,  8.15685425,  2.5], [-0.76598632, -0.76598632,  9.03197265]])
#init_point = np.array([[2,5,7],[2,4,3],[1,2,2],[3,8,9],[3,2,3],[6,6,5]])
init_point = np.array([[2.5,2.5,2.5]])
init_point =  pv.PointSet(init_point)

#creation of first streamline (REVIEW INITIAL AND MINIMYUM STEP LENGTH)
streamline = initial_streamline(mesh10_3, init_point, "forward", 0.2, 'cl', 0.2, 2000, 0)

#put cell data into queue as point data
streamline_points = streamline.cell_points(0)
queue.append(streamline_points)

#take out streamline from queue as base_streamline
base_streamline = queue[0]

#append streamline (as point data) to a list of streamlines for storage (this will be the final print-line list)

#add point data of streamline into unstructured grid representing 'taken' points

#remove streamline1 from queue


#pick point from selected streamline (base_streamline) (probably the first point in the dataset) as base_point
base_point = base_streamline[0]

#generate new points based on the base_point

#filter the new points to avoid collisions

#integrate the streamlines from the new points, taking care to avoid collisions

#append new streamlines to queue


#LOOP:
#while there are streamlines in queue:
#----assign streamline from queue to a variable representing the current streamline
#----append streamline (as point data) to a list of streamlines for storage (this will be the final print-line list)
#----add point data of streamline into unstructured grid represening 'taken' points
#----remove streamline from queue
#----initiate point queue (empty)
#----make queue of all possible seed points and filter them based on other streamlines
#----LOOP:
#----While point in seed points queue (starting from a logical first one, probably near the start of the base streamline):
#----#----assign point as variable seed_point
#----#----assign this point to set of seed-points
#----#----integrate the streamline from these seed-points, taking care to avoid collisions (using the same local collision function)
#----#----remove current point from queue
#----#----append new streamline to queue


#NOTES for later:
#There will be voids between streamlines of the actual component (although if the above sudo-code is implemented, then void should be avoided) (because they diverge). You will need to find these points and integrate from there. Perhaps, you can locate these
#points during the point filtering: i.e. if points are colliding, halt integration, if there is a distance breater than some distance, append the points to a set of 'void points'.
#this will not work, but can be adapted to work. It will not work since then we will be a whole lot of void points which may lie on the same streamline. Also, it would be better to
#incorporate ALL streamline generation within the main loop
"""
using separation distance between streamlines, define a set of points (probably a point cloud) that are a distance dsep away
from the base_point and on a line perpendicular to the vector at base_point. Also make sure that these newly defined points
are optimally spaced - meaning that they are all dsep away from eachother around the base point, but not to much more or too
much less. Finally check that the newly defined points are not within dtest*dsep of any points from other streamlines - but
don't check through all streamlies (this will take too long). Instead, check through the 27 cells found around each newly
defined point: this grid , called dsep_grid is made of cubic cells of side length dsep.
"""


"""finding vector at base point. Two options (1) based on mesh, but requires that the base point is on the mesh (2) interpolated, but there is a chance that it is badly behaived if the vector field is not nice. A mixture of the two methods could also be implemented """
""" option (1) """
#get index of base_point (so that you can then find vector)
#points = mesh10_3.points
#comparison = points == base_point
#index = np.where(np.all(comparison,axis=1))
#index = index[0][0]

#get vector at base_point


""" option (2) """
"""
#interpolate
vector_new = interpolator(mesh, u_list, v_list, w_list, init_point[0], init_point[1], init_point[2], method="nearest")
"""

"""
for the remaining seed_points (the points defiend and filtered in the previous comment will be in a array called 'seed_points' probably), begin
integration by using the interpolator function and at each step checking if the emerging points of the streamline are well separated - i.e. check
the 27 cells around the point (probably make this into a function)
"""

#testing

p = pv.Plotter()
p.add_mesh(mesh10_3.outline())
p.add_mesh(streamline.tube(radius=0.5))
p.show()

