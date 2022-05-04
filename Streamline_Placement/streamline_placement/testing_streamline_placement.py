import numpy as np
import pyvista as pv

from main_streamline_placement import streamline_placement
#from functions_streamline_placement import interpolator2
from functions_mesh_creation import mesh_creation
#from inputs_streamline_placement import *

"""--------------------INPUTS: MESH CREATION------------------------"""

nx = 10
ny = 10
nz = 10
datafileXmZM = "Test_Case2.csv"
datafileXMZm = ""
#output_vfield.csv              #Pyvista
#field_vect_scaledByDensity.csv #Scipy
"""--------------------INPUTS: STREAMLINE PLACEMENT------------------------"""

init_point = np.array([[0.,0.,0.]])

mesh_pyvista, mesh_scipy, u_list, v_list, w_list = mesh_creation(nx, ny, nz, datafileXmZM, datafileXMZm) #look a few lines above
#mesh = pv.UniformGrid(dims=(nx,ny,nz), spacing=(1,1,1), origin=(0,0,0))

#u_list, v_list, w_list, mesh = mesh_creation(nx, ny, nz, datafile) #look a few lines above
mesh = pv.UniformGrid(dims=(nx,ny,nz), spacing=(1,1,1), origin=(0,0,0))
#print(mesh)
integration_direction = "forward"
initial_step_length = 1
step_unit = "cl" #'cell length'
min_step_length = 1
max_steps = 2000
terminal_speed = 0
dsep = 0.25
radius = 0.5
n_seed_points = 4

"""--------------------CALLING FUNCTIONS------------------------"""




streamline_placement(init_point, mesh, u_list, v_list, w_list, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed, dsep, radius, n_seed_points)

