import pyvista as pv
import vtk
import numpy as np
import matplotlib
from vector_file_processing import *
pv.set_plot_theme("document")
pv.global_theme.outline_color = 'green'
dimensions = (95,59,36)

def extracted_mesh(mesh_pyvista, bounds):
    #bounds have format: (xmin, xmax, ymin, ymax, zmin, zmax)
    mesh_pyvista_extracted = mesh_pyvista.extract_subset(bounds)
    return mesh_pyvista_extracted

def mesh_adjustment(mesh):
    #make sure all associated w vectors for the parsed mesh are positive (i.e. pointing up)
    mesh['vectors'][:,0] = abs(mesh['vectors'][:,0])
    return mesh

def field_plotter(dimensions,datafile):
    #data file is csv file with columns: x y z scalar

    mesh = pv.UniformGrid(
        dims=dimensions,
        origin=(1.0, 1.0, 1.0)
    )
    direction_vectors, scalars = scaled_vector_processing(datafile)
    mesh['vectors'] = direction_vectors
    mesh['Scalars'] = scalars




    #mesh = mesh_adjustment(mesh)
    #print(mesh['Scalars'])

    #boundary = clipped.decimate_boundary().extract_all_edges()
    #mesh.set_active_scalars('Vectors')
    #streamlines, src = mesh.streamlines(
    #    return_source=True, source_radius=5, source_center=(59, 27, 2)
    #)

    arrows = mesh.glyph(orient="vectors", scale="Scalars")
    #(xmin, xmax, ymin, ymax, ,zmin zmax)
    bounds = [59, 79, 27, 44, 2, 22]
    clipped = arrows.clip_box(bounds)
    boundary = mesh.decimate_boundary().extract_all_edges()
    extracted = extracted_mesh(mesh, bounds)
    pl = pv.Plotter()
    #pl.add_mesh(streamlines.tube(radius=0.2), lighting=False)
    #pl.add_mesh(src)
    #pl.add_mesh(boundary, color="grey", opacity=0.25)
    #pl.camera_position = [(10, 9.5, -43), (87.0, 73.5, 123.0), (-0.5, -0.7, 0.5)]
    pl.add_mesh(arrows, label='Input', color='tan')
    #pl.add_mesh(clipped, style='wireframe', color='red', label='Clipped')
    pl.add_mesh(mesh.outline(), color='black')
    pl.add_mesh(extracted.outline(), color='black')
    pl.camera.position = (109.08918728934306, 104.94778806690199, 30.739613025075645)
    pl.show(screenshot='Test_2.png')

    return mesh, arrows, clipped

mesh, arrows, clipped = field_plotter(dimensions,"output_new_orientation.csv")
