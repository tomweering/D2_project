import compas
from compas.geometry import Point
from compas.geometry import Vector
import numpy as np

from VectorFilteringOrientation.grid_project import x, y, z, value_x, value_y, value_z

# grid = np.meshgrid(np.linspace(-1, 1, 3),
#                    np.linspace(-1, 1, 3),
#                    np.linspace(-2, 2, 5))
#
# x, y, z = grid

x_points = x.ravel()
y_points = y.ravel()
z_points = z.ravel()

print(np.shape(x), np.shape(value_x))

flat_vx = value_x.ravel()
flat_vy = value_y.ravel()
flat_vz = value_z.ravel()

points = np.array([x_points, y_points, z_points])
points = np.reshape(points, (len(x_points), 3))

vectors = np.array([flat_vx, flat_vy, flat_vz])
vectors = np.reshape(vectors, (len(flat_vx), 3))

compas_points = []
compas_vector = []
for i in range(len(points)):
    compas_points.append(Point(points[i][0], points[i][1], points[i][2]))
    compas_vector.append(Vector(vectors[i][0], vectors[i][1], vectors[i][2]))

compas.json_dump(compas_vector, 'rhino_plot_b1.json')
compas.json_dump(compas_points, 'rhino_plot_b2.json')
