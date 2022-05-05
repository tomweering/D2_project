import numpy as np
import pyvista as pv

from main_streamline_placement import streamline_placement
#from functions_streamline_placement import interpolator2
from functions_mesh_creation import mesh_creation
#from inputs_streamline_placement import *

"""--------------------INPUTS: MESH CREATION------------------------"""


nx = 95
ny = 59
nz = 36

#datafile = "Test_Case2.csv"

datafileXmZM = "output_vfield.csv"
datafileXMZm = "field_vect_scaledByDensity.csv"
#output_vfield.csv              #Pyvista
#field_vect_scaledByDensity.csv #Scipy


"""--------------------INPUTS: STREAMLINE PLACEMENT------------------------"""

init_point = np.array([[0.,0.,0.]])

mesh_pyvista, mesh_scipy, u_list, v_list, w_list = mesh_creation(nx, ny, nz, datafileXmZM, datafileXMZm) #look a few lines above
print(mesh_pyvista)
#mesh = pv.UniformGrid(dims=(nx,ny,nz), spacing=(1,1,1), origin=(0,0,0))

bounds = [59, 79, 27, 44, 2, 22]
clipped = mesh_pyvista.clip_box(bounds)
mesh_pyvista = clipped
print(clipped['vectors'])
integration_direction = "forward"
initial_step_length = 1
step_unit = "cl" #'cell length'
min_step_length = 1
max_steps = 2000
terminal_speed = 0
dsep = 0.25
radius = 0.5
#u_list, v_list, w_list = np.ones((1000,1)), np.ones((1000,1)), np.ones((1000,1))
#mesh['vectors'] = np.ones((1000,3))
n_seed_points = 4

"""--------------------CALLING FUNCTIONS------------------------"""




streamline_placement(init_point,  mesh_pyvista, mesh_scipy, u_list, v_list, w_list, integration_direction, initial_step_length, step_unit, min_step_length, max_steps, terminal_speed, dsep, radius, n_seed_points)


