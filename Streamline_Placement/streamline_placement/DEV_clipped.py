import numpy as np
import pyvista as pv

from main_streamline_placement import streamline_placement
from functions_streamline_placement import streamline
from functions_mesh_creation import mesh_creation, extracted_mesh, mesh_adjustment
#from inputs_streamline_placement import *

pv.set_plot_theme("document")
"""--------------------INPUTS: MESH CREATION------------------------"""


nx = 95
ny = 59
nz = 36

#datafile = "Test_Case2.csv"

datafileXmZM = "output_new_orientation.csv"
datafileXMZm = "field_vect_scaledByDensity.csv"
#output_vfield.csv              #Pyvista
#field_vect_scaledByDensity.csv #Scipy


"""--------------------INPUTS: STREAMLINE PLACEMENT------------------------"""



mesh_pyvista, mesh_scipy, u_list, v_list, w_list = mesh_creation(nx, ny, nz, datafileXmZM, datafileXMZm) #look a few lines above

bounds = [59, 79, 27, 44, 2, 22]

mesh_extracted = extracted_mesh(mesh_pyvista, bounds)
#mesh_extracted = mesh_adjustment(mesh_extracted)

init_point = [59.,27.,18]
streamlines_bracket = mesh_extracted.streamlines(vectors="vectors",n_points=1, source_radius=1.0,source_center=init_point, terminal_speed=0.0)
streamlines_bracket = streamline(mesh_extracted,pv.PointSet(init_point),"forward", 0.1,"cl", 0.1, 2000, 0.)
p = pv.Plotter()
p.add_mesh(streamlines_bracket.tube(radius=0.3), color='tan')
p.show()
#mesh = pv.UniformGrid(dims=(nx,ny,nz), spacing=(1,1,1), origin=(0,0,0))
#This clipping stuff does nothing, look above for extraction method
#bounds = [59, 79, 27, 44, 2, 22]
#clipped = mesh_pyvista.clip_box(bounds)
#print("clipped mesh", clipped)
#print("len clipped mesh vectors", len(clipped["vectors"]))
#print("numer of points in clipped", len(clipped.points))

#print(clipped)
integration_direction = "forward"
initial_step_length = 1.
step_unit = "cl" #'cell length'
min_step_length = 1.
max_steps = 1000000000
terminal_speed = 0.
dsep = 0.1
radius = 0.2
dsep_multiplier = 1
n_seed_points = 4


#dsep = dsep_multiplier*dsep
"""--------------------CALLING FUNCTIONS------------------------"""

if __name__ == '__main__':

    queue_streamlines, occupied_points, print_lines, mesh = streamline_placement(init_point,  mesh_extracted, mesh_scipy, u_list, v_list, w_list, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed, dsep, radius, n_seed_points)

    p = pv.Plotter()

    from functions_streamline_placement import lines_from_points
    for i in print_lines:
        p.add_mesh(lines_from_points(i).tube(radius=radius))
    p.show()