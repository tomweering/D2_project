
"""
.. _clip_with_plane_box_example:

Clipping with Planes & Boxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clip/cut any dataset using using planes or boxes.
"""
# sphinx_gallery_thumbnail_number = 2
import pyvista as pv
from pyvista import examples

dataset = examples.download_office()
print(dataset)
bounds = [0,1, 0, 4.5, 1, 3]
clipped = dataset.clip_box(bounds)
#print(clipped)
p = pv.Plotter()
p.add_mesh(dataset, style='wireframe', color='blue', label='Input')
p.add_mesh(clipped, label='Clipped')
#p.add_legend()
p.show()