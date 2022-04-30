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

    arrows = mesh.glyph(orient="Vectors", scale="Scalars")
    pl = pv.Plotter()
    actor = pl.add_mesh(arrows)
    #actor = pl.add_mesh(mesh)
    pl.show()
    return mesh, arrows

field_plotter(dimensions,"output_vfield.csv")