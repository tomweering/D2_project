from functions_streamline_placement import *
from inputs_streamline_placement import *

"""-----------------------------------------------------------"""
"""INPUTS THAT WE MAY WANT TO CHANGE MORE FREQUENTLY"""
n_seed_points = 4
Radius = 0.5
<<<<<<< HEAD
dsep = 0.25
mesh = mesh10_3np
#pyvista find vector at point#define separation distance, dsep, between streamlines and the checking parameter to avoid colisions, dtest (a proportional param. between 0 and 1)
dsep = 0.5 #cell unit lengths
dtest = 1 #proportion parameter
u_list = u_list
v_list = v_list
w_list = w_list
"""--------------------------------------------------------------"""
#initialising queue of streamlines
=======
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
>>>>>>> f1ba762d7208a11e585f3b0f17310a8cada744d4
queue_streamlines = []
# initialising set of finalised print-lines
print_lines = []

# definition of seed point for first streamline
init_point = np.array([[0, 0, 0]])
init_point = pv.PointSet(init_point)

<<<<<<< HEAD
#definition of seed point for frist streamline
init_point = np.array([[0,0,0]])
init_point =  pv.PointSet(init_point)
#print(init_point)

#creation of first streamline (REVIEW INITIAL AND MINIMYUM STEP LENGTH)
streamline1 = streamline(mesh10_3, init_point, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed)
#print(streamline1)
#streamline2 = streamline(mesh10_3, init_point, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed)
#convert streamline into a set of points
streamline_as_points = streamline1.cell_points(0)
#print(streamline_as_points)

#add point data of initial streamline into a set of points representing 'taken' points
occupied_points = np.empty([1,3])
occupied_points = np.append(occupied_points,streamline_as_points,axis=0)
print("occupied points",occupied_points)
occupied_points = np.delete(occupied_points, 0, 0)

print("streamline as points", streamline_as_points)
print("occupied points",occupied_points)

#Put inital streamline as first finalised print_line in 'print_lines'
=======
# creation of first streamline (REVIEW INITIAL AND MINIMUM STEP LENGTH)
streamline = initial_streamline(mesh10_3, init_point, 'forward', 0.2, 'cl', 0.2, 2000, 0)

# convert streamline into a set of points
streamline_as_points = streamline.cell_points(0)

# add point data of initial streamline into a set of points representing 'taken' points
occupied_points = streamline_as_points

# Put initial streamline as first finalised print_line in 'print_lines'
>>>>>>> f1ba762d7208a11e585f3b0f17310a8cada744d4
print_lines.append(streamline_as_points)

# put streamline into queue as a set of points which will be the first element in the queue
queue_streamlines.append(streamline_as_points)
<<<<<<< HEAD
#print(queue_streamlines)
#initialising visualisation
tubes = pv.MultiBlock()
p = pv.Plotter()
tubes.append(streamline1.tube(radius=0.5))
p.add_mesh(mesh10_3.outline())
"""BEGINNING OF LOOP"""

def streamline_placement(queue_streamlines, occupied_points, print_lines):
    while queue_streamlines:
        #rint(len(queue_streamlines))
        # take out streamline from queue as base_streamline
        base_streamline = queue_streamlines[0]
        del queue_streamlines[0]
        queue_base_points = list(base_streamline)
        #print(queue_base_points)
        #print(base_streamline)
        while queue_base_points:
            #for each point defining the streamline, find more points around it and integrate more streamlines
            base_point = queue_base_points[0]
            print("base point",base_point)
            #print(base_point)
            del queue_base_points[0]
            possible_seed_points = new_seed_points(n_seed_points, dsep,[base_point],mesh)
            print("possible_seed_points", possible_seed_points)
            filtered_seed_points = seed_point_filter(possible_seed_points,occupied_points, dsep)
            print("Filtered Seed points",filtered_seed_points)
            #integrate from the filtered seed_points while after each one, adding the resulting streamline (as points) to occupied_points, print_lines and queue
            if len(filtered_seed_points) == 0:
                print("empty")
            for i in filtered_seed_points:
                print("filtered point",i)
                i = pv.PointSet(i)
                #integrate streamline, without regard to collision
                current_streamline = streamline(mesh10_3, i, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed)
                #print(current_streamline)
                streamline_as_points = current_streamline.points
                #streamline_as_points = current_streamline.cell_points(0)
                print("streamline as points for each point",streamline_as_points)

                #cutting streamlines when they collide with others or they pass out of box(looping through each point, starting with the first point)
                index = 0
                if len(streamline_as_points) > 0:
                    while proximity_check(streamline_as_points[index], occupied_points, dsep) and index<(len(streamline_as_points)-1):
                        index += 1
                else:
                    break
                streamline_as_points = streamline_as_points[:index+1]
                print("Streamline as points shortened", streamline_as_points)

                occupied_points = np.append(occupied_points,streamline_as_points,axis=0)
                print(occupied_points)
                print("occupied points so far", occupied_points)
                print_lines.append(streamline_as_points)
                print("print lines so far", print_lines)
                #print(print_lines)

                queue_streamlines.append(streamline_as_points)
                #print(queue_streamlines)
                line = lines_from_points(streamline_as_points)
                tubes.append(line.tube(radius=0.5))
    p.add_mesh(tubes)
    p.show()
    return queue_streamlines, occupied_points, print_lines
            

#print(print_lines)

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

#initialising set of print-lines ('tubes')
#tubes = pv.MultiBlock()
#testing
#print(len(print_lines))
#set of print_lines, defined as a set of points for each individual print_line
#tubes.append(streamline1.tube(radius=0.5))


#p = pv.Plotter()
#p.add_mesh(mesh10_3.outline())
#p.add_mesh(tubes)
#p.show()
=======

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
>>>>>>> f1ba762d7208a11e585f3b0f17310a8cada744d4
