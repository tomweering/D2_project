# %%
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("field_vect_3.csv")


directions = df.values.tolist()
directions = directions + [[0,0,0]]

#print(len(directions))
#print(directions)

coordinates = []

#Sort method 1 

#for y in range(59)
#for x in range(95)
#for z in range(36)

for x in range(95):
    for y in range(59):
        for z in range(36):
            coordinate = [x, y, z]
            coordinates.append(coordinate)

#print(len(coordinates))
#print(len(directions))
#print(coordinates)

items =[]
x_coordinates = []
y_coordinates = []
z_coordinates = []
x_direction = []
y_direction = []
z_direction = []

for k in range(len(coordinates)):
    item = [coordinates[k][0],coordinates[k][1],coordinates[k][2],directions[k][0],directions[k][1],directions[k][2]]
    items.append(item)
    x_coordinates.append(coordinates[k][0])
    y_coordinates.append(coordinates[k][1])
    z_coordinates.append(coordinates[k][2])
    x_direction.append(directions[k][0])
    y_direction.append(directions[k][1])
    z_direction.append(directions[k][2])

    
#print(items)

real_items = []

for k in range(len(items)):
    if (directions[k][0] + directions[k][1] + directions[k][2]) != 0:
        real_items.append(items[k])

#print(real_items)




fig = plt.figure()
ax = fig.gca(projection='3d')

ax.quiver(x_coordinates, y_coordinates, z_coordinates, x_direction, y_direction, z_direction, length=0.1, normalize=True)

plt.show()
            


# %%
