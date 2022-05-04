import pyvista as pv
import vtk
import numpy as np
import matplotlib
from vector_file_processing import *

dimensions = (95,59,36)

def field_plotter(dimensions,datafile):
    #data file is csv file with columns: x y z scalar

    mesh = pv.UniformGrid(
        dims=dimensions,
        origin=(1.0, 1.0, 1.0)
    )
    direction_vectors, scalars = scaled_vector_processing(datafile)
    mesh['Vectors'] = direction_vectors
    mesh['Scalars'] = scalars


    #boundary = clipped.decimate_boundary().extract_all_edges()
    #mesh.set_active_scalars('Vectors')
    #streamlines, src = mesh.streamlines(
    #    return_source=True, source_radius=5, source_center=(59, 27, 2)
    #)

    arrows = mesh.glyph(orient="Vectors", scale="Scalars")
    #(xmin, xmax, ymin, ymax, ,zmin zmax)
    bounds = [59, 79, 27, 44, 2, 22]
    clipped = arrows.clip_box(bounds)
    boundary = mesh.decimate_boundary().extract_all_edges()
    pl = pv.Plotter()
    #pl.add_mesh(streamlines.tube(radius=0.2), lighting=False)
    #pl.add_mesh(src)
    pl.add_mesh(boundary, color="grey", opacity=0.25)
    #pl.camera_position = [(10, 9.5, -43), (87.0, 73.5, 123.0), (-0.5, -0.7, 0.5)]
    pl.add_mesh(arrows,  style='wireframe', color='blue', label='Input')
    pl.add_mesh(clipped, style='wireframe', color='red', label='Clipped')
    pl.show()

    return mesh, arrows, clipped

mesh, arrows, clipped = field_plotter(dimensions,"output_vfield.csv")