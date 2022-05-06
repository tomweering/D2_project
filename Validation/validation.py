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

def streamline_length(n,i):

    Locallenghts = []

    for j in range(len(n[i])-1):
        x = list_of_streamlines[i][j][0]
        x_1 = list_of_streamlines[i][j+1][0]
        y = list_of_streamlines[i][j][1]
        y_1 = list_of_streamlines[i][j+1][0]
        z = list_of_streamlines[i][j][2]
        z_1 = list_of_streamlines[i][j+1][0]

        LocalLenght = np.sqrt((x_1 - x)**2 + (y_1 - y)**2 + (z_1 - z)**2) 
        Locallenghts.append(LocalLenght)

    streamline_length = sum(Locallenghts)

    return(streamline_length) 




list_of_streamlines = []


for i in range(20):
    list_of_streamlines.append(random_streamline_point(randint(0,10),randint(0,10),randint(0,10),randint(10,40)))

#print(list_of_streamlines)

Locallenghts = []
Totallength = []
streamline_lengths = []

upper_bound_area = 0.5 #[mm^2]
lower_bound_area = 0.1 #[mm^2]

j = 0

#computing segments lenght and adding it to total
#fix indentation of j... causes error where only first length is computed
for i in range(len(list_of_streamlines)):
    streamline_lengths.append(streamline_length(list_of_streamlines,i))

            
#print(Locallenghts)
#print(sum(Locallenghts)) #[mm] ? 
print(streamline_lengths)


upper_estimate_volume = upper_bound_area * sum(streamline_lengths)
lower_estimate_volume = lower_bound_area * sum(streamline_lengths)

lug_volume = 6.626E+07 #[mm^3]

#results
print(f"the upper streamlines to lug volume ratio is: {(upper_estimate_volume/lug_volume)*100} %")
print(f"the upper streamlines to lug volume ratio is: {(lower_estimate_volume/lug_volume)*100} %")
#print("the upper streamlines to lug volume ratio is:", (sum(LocalVolumes)/lug_volume)*100, "%")
#print("there are ", len(streamlines), "streamlines ranging between", min(LocalLenghts), "and", max(LocalLenghts))