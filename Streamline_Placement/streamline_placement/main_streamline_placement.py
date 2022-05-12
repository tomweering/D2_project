from functions_streamline_placement import *

# from inputs_streamline_placement import *
"""-----------------------------------------------------------"""
"""INPUTS THAT WE MAY WANT TO CHANGE MORE FREQUENTLY"""
# n_seed_points = 4
# Radius = 0.5
# dsep = 0.25
# mesh = mesh10_3np
# pyvista find vector at point#define separation distance, dsep, between streamlines and the checking parameter to avoid colisions, dtest (a proportional param. between 0 and 1)
# dsep = 0.5 #cell unit lengths
# dtest = 1 #proportion parameter
# u_list = u_list
# v_list = v_list
# w_list = w_list
"""--------------------------------------------------------------"""
"""
#initialising queue of streamlines
queue_streamlines = []
#initialising set of finalised print-lines
print_lines = []
#definition of seed point for frist streamline
init_point = np.array([[9.,9.,9.]])
init_point =  pv.PointSet(init_point)
#creation of first streamline (REVIEW INITIAL AND MINIMYUM STEP LENGTH)
streamline1 = streamline(mesh10_3, init_point, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed)
#convert streamline into a set of points
streamline_as_points = streamline1.cell_points(0)
#add point data of initial streamline into a set of points representing 'taken' points
occupied_points = np.empty([1,3])
occupied_points = np.append(occupied_points,streamline_as_points,axis=0)
occupied_points = np.delete(occupied_points, 0, 0)
#Put inital streamline as first finalised print_line in 'print_lines'
print_lines.append(streamline_as_points)
#put streamline into queue as a set of points which will be the first element in the queue
queue_streamlines.append(streamline_as_points)
#initialising visualisation
tubes = pv.MultiBlock()
p = pv.Plotter()
tubes.append(streamline1.tube(radius=Radius))
p.add_mesh(mesh10_3.outline())
"""
"""BEGINNING OF LOOP"""


def streamline_placement(init_point, mesh_pyvista, mesh_scipy, u_list, v_list, w_list, integration_direction,
                         initial_step_length, step_unit, min_step_length, max_steps, terminal_speed, dsep, radius,
                         n_seed_points):
    # initialising queue of streamlines
    queue_streamlines = []
    # initialising set of finalised print-lines
    print_lines = []

    init_point = pv.PointSet(init_point)

    # creation of first streamline (REVIEW INITIAL AND MINIMUM STEP LENGTH)
    streamline1 = streamline(mesh_pyvista, init_point, integration_direction, initial_step_length, step_unit,
                             min_step_length, max_steps, terminal_speed)

    # streamline1 = mesh_pyvista.streamlines(vectors="vectors", source_center=None, source_radius=None, n_points=1,start_position=init_point.points[0], return_source=False, pointa=None,pointb=None, progress_bar=False)
    # convert streamline into a set of points
    streamline_as_points = streamline1.points

    # add point data of initial streamline into a set of points representing 'taken' points
    occupied_points = np.empty([1, 3])
    occupied_points = np.append(occupied_points, streamline_as_points, axis=0)

    occupied_points = np.delete(occupied_points, 0, 0)

    # Put inital streamline as first finalised print_line in 'print_lines'
    print_lines.append(streamline_as_points)

    # put streamline into queue as a set of points which will be the first element in the queue
    queue_streamlines.append(streamline_as_points)
    # initialising visualisation

    si = 0
    while len(queue_streamlines) > 0:
        #print(f'len of queue of streamlines {len(queue_streamlines)}')
        #print(f'Streamline iterator {si}')
        si += 1
        # print(queue_streamlines)
        # rint(len(queue_streamlines))
        # take out streamline from queue as base_streamline
        base_streamline = queue_streamlines[0]
        queue_streamlines.pop(0)
        queue_base_points = list(base_streamline)
        # print(queue_base_points)
        # print(base_streamline)
        bpi = 0
        while len(queue_base_points) > 0:

            #print(f'Base_point iterator{bpi}')
            bpi += 1
            # for each point defining the streamline, find more points around it and integrate more streamlines
            base_point = queue_base_points[0]
            # print(base_point)
            queue_base_points.pop(0)
            base_vector = interpolator2(mesh_pyvista, base_point)
            #print("magnitude of base_vector", np.linalg.norm(base_vector))
            if np.linalg.norm(base_vector) == 0.:
                #print("VECTOR AT THIS BASEPOINT IS 0")
                continue
            possible_seed_points = new_seed_points(n_seed_points, dsep, base_point, mesh_pyvista, mesh_scipy, u_list,
                                                   v_list, w_list)
            #print("possible", possible_seed_points)
            # print(possible_seed_points)

            # print("possible_seed_points", possible_seed_points)
            filtered_seed_points = seed_point_filter(possible_seed_points, occupied_points, dsep, mesh_pyvista)
            #print("number of filtered base points", len(filtered_seed_points))
            # print("Filtered Seed points",filtered_seed_points)
            # integrate from the filtered seed_points while after each one, adding the resulting streamline (as points) to occupied_points, print_lines and queue
            # if len(filtered_seed_points) == 0:
            # print("empty")

            for i in filtered_seed_points:
                print(f'seed point{i}')
                print("i", i)
                # print("filtered point",i)
                i = pv.PointSet(i)
                # integrate streamline, without regard to collision

                current_streamline = streamline(mesh_pyvista, i, integration_direction, initial_step_length, step_unit,
                                                min_step_length, max_steps, terminal_speed)
                # print(current_streamline)
                streamline_as_points = current_streamline.points
                # print("streamline as points",streamline_as_points)
                # streamline_as_points = current_streamline.cell_points(0)
                # print("streamline as points for each point",streamline_as_points)

                # cutting streamlines when they collide with others or they pass out of box(looping through each point, starting with the first point)
                #print(((len(streamline_as_points) - 1) * initial_step_length), (0.5 * min(mesh_pyvista.dimensions)))
                if ((len(streamline_as_points) - 1) * initial_step_length) > (0.5 * min(mesh_pyvista.dimensions)):
                    index = 0
                    while (proximity_check(streamline_as_points[index], occupied_points, dsep) == True) and index < (
                            len(streamline_as_points) - 1):
                        index += 1
                    streamline_as_points = streamline_as_points[:(index)]
                    #for i in streamline_as_points:
                        #print(proximity_check(i, occupied_points, dsep))
                    if ((len(streamline_as_points) - 1) * initial_step_length) > (0.5 * min(mesh_pyvista.dimensions)):
                        #print(f'length of current streamline{len(streamline_as_points)}')
                        # print("Streamline as points shortened", streamline_as_points)
                        #print("len streamline as points minus 1 multipled by step units",
                              #(len(streamline_as_points) - 1) * initial_step_length)
                        #print("minimum of mesh pyvista dimensions divided by two", (0.5 * min(mesh_pyvista.dimensions)))
                        occupied_points = np.append(occupied_points, streamline_as_points, axis=0)
                        print_lines.append(streamline_as_points)
                        queue_streamlines.append(streamline_as_points)

    return queue_streamlines, occupied_points, print_lines, mesh_pyvista

# print(print_lines)

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
# tubes = pv.MultiBlock()
# testing
# print(len(print_lines))
# set of print_lines, defined as a set of points for each individual print_line
# tubes.append(streamline1.tube(radius=0.5))


# p = pv.Plotter()
# p.add_mesh(mesh10_3.outline())
# p.add_mesh(tubes)
# p.show()