# %%
#import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import csv

direction_list = []
direction = []
coordinates = []
items = []

with open("field_vect_scaledByDensity.csv","r",newline='') as f:

        csvReader = csv.reader(f,delimiter=',')
        for row in csvReader:
            direction_list.append(row)

        for row in range(len(direction_list)):
            direction_x = float(direction_list[row][0])
            direction_y = float(direction_list[row][1])
            direction_z = float(direction_list[row][2])
            direction_component = [ direction_x, direction_y, direction_z]
            direction.append(direction_component)

print(len(direction))


for x in range(95):
    for y in range(59):
        for z in range(36):
            coordinate = [x, y, z]
            coordinates.append(coordinate)
print(len(coordinates))

for k in range(len(coordinates)):
    item = [coordinates[k][0],coordinates[k][1],coordinates[k][2],direction[k][0],direction[k][1],direction[k][2]]
    items.append(item)



new_list = sorted(items , key=lambda k: [k[2], k[1], k[0]])

print(new_list)

new_items = []

for i in range(len(new_list)):
    new_item = [new_list[i][3],new_list[i][4],new_list[i][5]]
    new_items.append(new_item)

new_coordinates = np.array(new_items)
<<<<<<< Updated upstream
np.savetxt("new_organized_field_vect.csv", new_coordinates,delimiter=",")
=======
np.savetxt("Test_Case_Scipy.csv", new_coordinates, delimiter=",")
>>>>>>> Stashed changes
