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

lug_volume = 66262.085 #[mm^3]
leg_volume = 5054.321 #[mm^3]

# ============================================================================================================

#s = r"C:\Users\vargs\Downloads\D2Project-main (3)\D2Project-main\archive\Streamlines_LowResolution.csv"


s = r"Validation\Streamlines_LowResolution.csv"

int_time = np.genfromtxt(s, skip_header=1, usecols=[3], delimiter=',')
points_xyz = np.transpose(np.genfromtxt(s, skip_header=1, usecols=(12, 13, 14), delimiter=','))

mask = np.ones(len(int_time)) #has zeros where integration time = 0 and ones where integration time != 0
mask[np.where(int_time == 0)] = 0

gradient_mask = np.diff(mask) #takes a difference a[i+1] - a[i] for all i. Effectively it's a gradient of mask

mask_start = np.where(gradient_mask > 0.0) #integration time goes from 0 to smth non-zero: streamline starts
mask_stop = np.where(gradient_mask < 0.0) ##integration time goes from smth non-zero to 0: streamline stops

streamlines_x =[]
streamlines_y = []
streamlines_z = []

for i in range(len(mask_start[0])):
    new_x = points_xyz[0][mask_start[0][i] : mask_stop[0][i]]#start_point:end_point
    new_y = points_xyz[1][mask_start[0][i] : mask_stop[0][i]]
    new_z = points_xyz[2][mask_start[0][i] : mask_stop[0][i]]

    streamlines_x.append(new_x)
    streamlines_y.append(new_y)
    streamlines_z.append(new_z)



def streamline_splitting_length(streamline_x,streamline_y,streamline_z,j,Bx_1,By_1,Bx_2,By_2,Bz_1,Bz_2):
    x = 0
    x_1= 0
    y = 0
    y_1 = 0
    z = 0
    z_1 = 0

    streamline_splitting_lengths = []
    
    for i in range(len(streamline_x[j])-1):
        if Bx_1 <= streamline_x[j][i] <= Bx_2 and By_1 <= streamline_y[j][i] <= By_2 and Bz_1 <= streamline_z[j][i] <= Bz_2:
            x = streamline_x[j][i]
            x_1= streamline_x[j][i+1]
            y = streamline_y[j][i]
            y_1 = streamline_y[j][i+1]
            z = streamline_z[j][i+1]
            z_1 = streamline_z[j][i+1]
            streamline_splitting_length = np.sqrt((x_1 - x)**2 + (y_1 - y)**2 + (z_1 - z)**2)
            streamline_splitting_lengths.append(streamline_splitting_length)

    streamline_splitting_lengths_sum = sum(streamline_splitting_lengths)

    return(streamline_splitting_lengths_sum)
    

a_list_of_streamline_lengths = []


"""Bounding Box Dimensions"""
Bx_1 = -49.18609 #[mm]
Bx_2 = -9.18609 #[mm]
By_1 = -24.232828 #[mm]
By_2 = 9.767172#[mm]
Bz_1 = -0.077015 #[mm]
Bz_2 = 39.922985 #[mm]


for j in range(len(streamlines_x)):
    a_list_of_streamline_lengths.append(streamline_splitting_length(streamlines_x,streamlines_y,streamlines_z,j,Bx_1,By_1,Bx_2,By_2,Bz_1,Bz_2))


#print(a_list_of_streamline_lengths)

upper_estimate_volume_test = sum(a_list_of_streamline_lengths)*upper_bound_area 
lower_estimate_volume_test = sum(a_list_of_streamline_lengths)*lower_bound_area 




#results
#print(f"the upper streamlines to lug volume ratio is: {(upper_estimate_volume_test/lug_volume)*100} %")
#print(f"the upper streamlines to lug volume ratio is: {(lower_estimate_volume_test/lug_volume)*100} %")
print(f"the upper streamlines to leg volume ratio is: {(upper_estimate_volume_test/leg_volume)*100} %")
print(f"the upper streamlines to leg volume ratio is: {(lower_estimate_volume_test/leg_volume)*100} %")
#print("the upper streamlines to lug volume ratio is:", (sum(LocalVolumes)/lug_volume)*100, "%")
#print("there are ", len(streamlines), "streamlines ranging between", min(LocalLenghts), "and", max(LocalLenghts))


import matplotlib.pyplot as plt
import numpy as np

print("The AVERAGE streamline lenght is", np.average(a_list_of_streamline_lengths), "mm")
print("The LONGEST streamline lenght is", max(a_list_of_streamline_lengths), "mm")
print("The SHORTEST streamline lenght is", min(a_list_of_streamline_lengths), "mm")

#streamline_lengths = [78, 94, 28, 57, 48, 89, 91, 47, 47, 84, 55]
distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
maximum = max(a_list_of_streamline_lengths)
minimum = min(a_list_of_streamline_lengths)
step = (maximum - minimum) / 10
silvio = []
for i in range(10):
    silvio.append(maximum - (step * i))
print(silvio)
for value in a_list_of_streamline_lengths:
    for i in range(10):
        if value >= maximum - (step * (i+1)):
            distribution[i] += 1
            break



plt.bar(silvio, distribution)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution')
plt.show()