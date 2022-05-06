
"""
.. _clip_with_plane_box_example:

Clipping with Planes & Boxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clip/cut any dataset using using planes or boxes.
"""
# sphinx_gallery_thumbnail_number = 2
import pyvista as pv
from pyvista import examples

mesh = examples.download_blood_vessels().cell_data_to_point_data()
mesh.set_active_scalars("velocity")
streamlines, src = mesh.streamlines(
    return_source=True, source_radius=10, source_center=(92.46, 74.37, 135.5)
)
boundary = mesh.decimate_boundary().extract_all_edges()

sargs = dict(vertical=True, title_font_size=16)
p = pv.Plotter()
p.add_mesh(streamlines.tube(radius=0.2), lighting=False, scalar_bar_args=sargs)
p.add_mesh(src)
p.add_mesh(boundary, color="grey", opacity=0.25)
p.camera_position = [(10, 9.5, -43), (87.0, 73.5, 123.0), (-0.5, -0.7, 0.5)]

p.show()

#p = pv.Plotter()
#p.add_mesh(dataset, style='wireframe', color='blue', label='Input')
#p.add_mesh(clipped, label='Clipped')
#p.add_legend()
#p.show()