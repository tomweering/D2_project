import numpy as np
from random import randint

def random_streamline_point(x,y,z,n):
    streamline_points = []

    for i in range(n):
        item = [x,y,z]
        streamline_points.append(item)
        x += randint(0,1)
        y += randint(0,1)
        z += randint(0,1)
    
    #streamline_points_array = np.array(streamline_points)

    return(streamline_points)


list_of_streamlines = []


for i in range(20):
    list_of_streamlines.append(random_streamline_point(randint(0,10),randint(0,10),randint(0,10),randint(10,40)))

Locallenghts = []
Totallength = []


#computing segments lenght and adding it to total
for i in range(len(list_of_streamlines)):
    for j in range(len(list_of_streamlines[i])-1):
        LocalLenght = 0
        LocalLenght = np.sqrt((list_of_streamlines[i][j+1][0] - list_of_streamlines[i][j][0])**2 + (list_of_streamlines[i][j+1][1] - list_of_streamlines[i][j][1])**2 + (list_of_streamlines[i][j+1][2] - list_of_streamlines[i][j][2])**2)
        Locallenghts.append(LocalLenght)
            
#print(Locallenghts)
#print(sum(Locallenghts)) #[mm] ? 

upper_bound_area = 0.5 #[mm^2]
lower_bound_area = 0.1 #[mm^2]

upper_estimate_volume = upper_bound_area * sum(Locallenghts)
lower_estimate_volume = lower_bound_area * sum(Locallenghts)

lug_volume = 6.626E+07 #[mm^3]

#results
print("the upper streamlines to lug volume ratio is:", (upper_estimate_volume/lug_volume)*100, "%")
print("the lower streamlines to lug volume ratio is:", (lower_estimate_volume/lug_volume)*100, "%")
#print("there are ", len(streamlines), "streamlines ranging between", min(LocalLenghts), "and", max(LocalLenghts))