import pyvista as pv
import vtk
import numpy as np
import matplotlib
from vector_file_processing import *
pv.set_plot_theme("document")
dimensions = (95, 59, 36)


def field_plotter(dimensions, datafile):
    # data file is csv file with columns: x y z scalar

    mesh = pv.UniformGrid(
        dims=dimensions,
        origin=(1.0, 1.0, 1.0)
    )
    direction_vectors, scalars = scaled_vector_processing(datafile)
    mesh['Vectors'] = direction_vectors
    mesh['Scalars'] = scalars

    arrows = mesh.glyph(orient="Vectors", scale="Scalars")
    # (xmin, xmax, ymin, ymax, ,zmin zmax)
    bounds = [59, 79, 27, 44, 2, 22]
    # bounds = [76, 79, 40, 44, 6, 9]
    # bounds = [59, 62, 27, 30, 18, 20]
    clipped = arrows.clip_box(bounds)

    pl = pv.Plotter()
    # pl.add_mesh(boundary, color="grey", opacity=0.25)
    # pl.camera_position = [(10, 9.5, -43), (87.0, 73.5, 123.0), (-0.5, -0.7, 0.5)]
    pl.add_mesh(arrows, color='tan')
    pl.camera.position = (130, 50, 160)
    pl.camera.zoom(8)
    pl.show(screenshot='Tan_Arrows_UnOrganized3.png')


    return mesh, arrows, clipped


mesh, arrows, clipped = field_plotter(dimensions, "output_new_unoriented2.csv")
