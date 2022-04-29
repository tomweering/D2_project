from functions_streamline_placement import *
from inputs_streamline_placement import *

"""-----------------------------------------------------------"""
"""INPUTS THAT WE MAY WANT TO CHANGE MORE FREQUENTLY"""
n_seed_points = 4
Radius = 0.5
mesh = mesh10_3
# pyvista find vector at point#define separation distance, dsep, between streamlines and the checking parameter to
# avoid collisions, dtest (a proportional param. between 0 and 1)
dsep: float = 0.5  # cell unit lengths
dtest: int = 1  # proportion parameter
# u_list: object = u_list
# v_list: object = v_list
# w_list: object = w_list
"--------------------------------------------------------------"
# initialising queue of streamlines
queue_streamlines = []
# initialising set of finalised print-lines
print_lines = []

# definition of seed point for first streamline
init_point = np.array([[0, 0, 0]])
init_point = pv.PointSet(init_point)

# creation of first streamline (REVIEW INITIAL AND MINIMUM STEP LENGTH)
streamline = initial_streamline(mesh10_3, init_point, 'forward', 0.2, 'cl', 0.2, 2000, 0)

# convert streamline into a set of points
streamline_as_points = streamline.cell_points(0)

# add point data of initial streamline into a set of points representing 'taken' points
occupied_points = streamline_as_points

# Put inital streamline as first finalised print_line in 'print_lines'
print_lines.append(streamline_as_points)

# put streamline into queue as a set of points which will be the first element in the queue
queue_streamlines.append(streamline_as_points)

"BEGINNING OF LOOP"
while queue_streamlines:
    # take out streamline from queue as base_streamline
    base_streamline = queue_streamlines[0]
    del queue_streamlines[0]
    queue_base_points = list(base_streamline)
    while queue_base_points:
        " for each point defining the streamline, find more points around it and integrate more streamlines "
        base_point = queue_base_points[0]
        print(base_point)
        del queue_base_points[0]
        possible_seed_points = new_seed_points(n_seed_points, Radius, [base_point], mesh10_3np)
        print(possible_seed_points)
        filtered_seed_points = seed_point_filter(possible_seed_points, occupied_points, dsep)
        # integrate from the filtered seed_points while after each one, adding the resulting streamline (as points)
        # to occupied_points, print_liens and queue

# LOOP:
# while there are streamlines in queue:
# ----assign streamline from queue to a variable representing the current streamline
# ----append streamline (as point data) to a list of streamlines for storage (this will be the final print-line list)
# ----add point data of streamline into unstructured grid represening 'taken' points
# ----remove streamline from queue
# ----initiate point queue (empty)
# ----make queue of all possible seed points and filter them based on other streamlines
# ----LOOP:
# ----While point in seed points queue (starting from a logical first one, probably near the start of the base streamline):
# ----#----assign point as variable seed_point
# ----#----assign this point to set of seed-points
# ----#----integrate the streamline from these seed-points, taking care to avoid collisions (using the same local collision function)
# ----#----remove current point from queue
# ----#----append new streamline to queue


# initialising set of print-lines ('tubes')
tubes = pv.MultiBlock()
# testing

# set of print_lines, defined as a set of points for each individual print_line
tubes.append(streamline.tube(radius=0.5))
tubes.append(lines_from_points(np.array([[3., 6., 2.], [8., 8., 1.]])).tube(radius=0.5))
tubes.append(lines_from_points([[3., 9., 9.], [2., 6., 8.]]).tube(radius=0.5))

p = pv.Plotter()
p.add_mesh(mesh10_3.outline())
p.add_mesh(tubes)
p.show()
