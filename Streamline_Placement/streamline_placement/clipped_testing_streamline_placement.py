import numpy as np
import pyvista as pv

from main_streamline_placement import streamline_placement
from functions_mesh_creation import mesh_creation

"""--------------------INPUTS: MESH CREATION------------------------"""

nx = 95
ny = 59
nz = 36

#datafileXmZM = "output_new_orientation.csv"
datafileXmZM = "output_new_unoriented2.csv"
datafileXMZm = "field_vect_scaledByDensity.csv"
# output_vfield.csv              #Pyvista
# field_vect_scaledByDensity.csv #Scipy


"""--------------------INPUTS: STREAMLINE PLACEMENT------------------------"""
pv.set_plot_theme("document")

mesh_pyvista, mesh_scipy, u_list, v_list, w_list = mesh_creation(nx, ny, nz, datafileXmZM, datafileXMZm)

init_point = [47.5, 29.5, 18.0]

streamlines_bracket = mesh_pyvista.streamlines(vectors='vectors', n_points=25000, source_radius=50,
                                               source_center=init_point, terminal_speed=0.0)
p = pv.Plotter(off_screen=True)
p.add_mesh(streamlines_bracket.tube(radius=0.08), color='tan')
#p.save_graphic(filename = "Final_tan.pdf", title = "Render of arbitrarily seeded streamlines using 45 Runge Kutta")
#p.add_mesh(mesh_pyvista.outline())
p.show(screenshot='Tan_Bracket_Unorganized.png')


"""--------------------CALLING FUNCTIONS------------------------"""

# streamline_placement(init_point,  mesh_pyvista, mesh_scipy, u_list, v_list, w_list, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed, dsep, radius, n_seed_points)
