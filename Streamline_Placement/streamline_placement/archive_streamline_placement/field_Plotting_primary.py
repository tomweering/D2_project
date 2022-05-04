import pyvista as pv
import vtk
import numpy as np
import matplotlib
from vector_file_processing import *

dimensions = (95,59,36)

def field_plotter(dimensions,datafile):
    #data file is csv file with columns: x y z scalar

    mesh = pv.UniformGrid(
        dims=dimensions
    )
    direction_vectors, scalars = scaled_vector_processing(datafile)
    mesh['Vectors'] = direction_vectors
    mesh['Scalars'] = scalars
    #print(mesh)
    arrows = mesh.glyph(orient="Vectors", scale="Scalars")
    #print(arrows)
    #(xmin, xmax, ymin, ymax, ,zmin zmax)
    bounds = [59, 79, 27, 44, 2, 22]
    clipped = arrows.clip_box(bounds)
    pl = pv.Plotter()
    pl.add_mesh(arrows,  style='wireframe', color='blue', label='Input')
    pl.add_mesh(clipped, style='wireframe', color='red', label='Clipped')
    pl.show()
    #print(arrows)
    #print(clipped)
    return mesh, arrows, clipped

mesh, arrows, clipped = field_plotter(dimensions,"output_vfield.csv")