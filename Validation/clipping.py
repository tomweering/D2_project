import numpy as np
import pyvista as pv
from functions_streamline_placement import lines_from_points
from main_streamline_placement import streamline_placement
from functions_streamline_placement import streamline
from functions_mesh_creation import mesh_creation, extracted_mesh, mesh_adjustment


s = r"Validation\Streamlines_LowResolution.csv"

int_time = np.genfromtxt(s, skip_header=1, usecols=[3], delimiter=',')
points_xyz = np.transpose(np.genfromtxt(s, skip_header=1, usecols=(12, 13, 14), delimiter=','))

mask = np.ones(len(int_time)) #has zeros where integration time = 0 and ones where integration time != 0
mask[np.where(int_time == 0)] = 0

gradient_mask = np.diff(mask) #takes a difference a[i+1] - a[i] for all i. Effectively it's a gradient of mask

mask_start = np.where(gradient_mask > 0.0) #integration time goes from 0 to smth non-zero: streamline starts
mask_stop = np.where(gradient_mask < 0.0) ##integration time goes from smth non-zero to 0: streamline stops

streamlines_x =[]
streamlines_y = []
streamlines_z = []
caroline_print_lines = []

for i in range(len(mask_start[0])):
    new_x = points_xyz[0][mask_start[0][i] : mask_stop[0][i]]#start_point:end_point
    new_y = points_xyz[1][mask_start[0][i] : mask_stop[0][i]]
    new_z = points_xyz[2][mask_start[0][i] : mask_stop[0][i]]

    streamlines_x.append(new_x)
    streamlines_y.append(new_y)
    streamlines_z.append(new_z)
    #caroline_print_line = [new_x, new_y, new_z]
    #caroline_print_lines.append(caroline_print_line)



def appendah(alist,blist,clist):
    caroline_print_streamlines = [] 

    for i in range(len(alist)):
        caroline_print_line = [alist[i], blist[i] , clist[i]]
        caroline_print_streamlines.append(caroline_print_line)
    
    return(caroline_print_streamlines)




for j in range(len(streamlines_x)):
    caroline_print_lines.append(appendah(streamlines_x[j],streamlines_y[j],streamlines_z[j]))


p = pv.Plotter()
radius = 0.1

print(caroline_print_lines[10])


for j in range(len(caroline_print_lines)):
    for i in caroline_print_lines[j]:
        p.add_mesh(lines_from_points(i).tube(radius=radius))
p.show()

