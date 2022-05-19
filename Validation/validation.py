import numpy as np
from random import randint
from lists_of_streamlines import print_lines

def streamline_length(n,i):

    Locallenghts = []

    for j in range(len(n[i])-1):
        x = n[i][j][0]
        x_1 = n[i][j+1][0]
        y = n[i][j][1]
        y_1 = n[i][j+1][0]
        z = n[i][j][2]
        z_1 = n[i][j+1][0]

        LocalLenght = np.sqrt((x_1 - x)**2 + (y_1 - y)**2 + (z_1 - z)**2) 
        Locallenghts.append(LocalLenght)

    streamline_length = sum(Locallenghts)

    return(streamline_length) 

Locallenghts = []
Totallength = []
streamline_lengths = []

upper_bound_area = np.pi * (0.5)**2 #[mm^2]
lower_bound_area = np.pi * (0.1)**2 #[mm^2]

j = 0

#computing segments lenght and adding it to total
#fix indentation of j... causes error where only first length is computed
for i in range(len(print_lines)):
    streamline_lengths.append(streamline_length(print_lines,i))

            
#print(Locallenghts)
#print(sum(Locallenghts)) #[mm] ? 
#print(streamline_lengths)


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
#Bx_1 = -49.18609 #[mm] LEG
Bx_1 = -167.186099 #[mm]
#Bx_2 = -9.18609 #[mm] LEG
Bx_2 = 19.129499 #[mm]
By_1 = -78.232828 #[mm]
#By_1 = -24.232828 #[mm]
By_2 = 37.478964#[mm]
#By_2 = 9.767172#[mm]
Bz_1 = -4.077015 #[mm]
#Bz_1 = -0.077015 #[mm]
Bz_2 = 66.526791 #[mm]
#Bz_2 = 39.922985 #[mm]


for j in range(len(streamlines_x)):
    a_list_of_streamline_lengths.append(streamline_splitting_length(streamlines_x,streamlines_y,streamlines_z,j,Bx_1,By_1,Bx_2,By_2,Bz_1,Bz_2))



upper_estimate_volume_test = sum(a_list_of_streamline_lengths)*upper_bound_area 
lower_estimate_volume_test = sum(a_list_of_streamline_lengths)*lower_bound_area 



print(f"the upper streamlines to full volume ratio is: {(upper_estimate_volume/lug_volume)*100} %")
print(f"the lower streamlines to full volume ratio is: {(lower_estimate_volume/lug_volume)*100} %")
print(f"the upper CAROLINE streamlines to full volume ratio is: {(upper_estimate_volume_test/lug_volume)*100} %")
print(f"the lower CAROLINE streamlines to full volume ratio is: {(lower_estimate_volume_test/lug_volume)*100} %")


import matplotlib.pyplot as plt
import numpy as np


print("The AVERAGE CAROLINE streamline lenght is", np.average(a_list_of_streamline_lengths), "mm")
print("The LONGEST CAROLINE streamline lenght is", max(a_list_of_streamline_lengths), "mm")
print("The SHORTEST CAROLINE streamline lenght is", min(a_list_of_streamline_lengths), "mm")

print("The AVERAGE streamline lenght is", np.average(streamline_lengths), "mm") 
print("The LONGEST streamline lenght is", max(streamline_lengths), "mm")
print("The SHORTEST streamline lenght is", min(streamline_lengths), "mm")

distribution_caroline = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tenpercentdistribution_caroline = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

distribution_us = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tenpercentdistribution_us = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

maximum_caroline = max(a_list_of_streamline_lengths)
minimum_caroline = min(a_list_of_streamline_lengths)

maximum_us = max(streamline_lengths)
minimum_us = min(streamline_lengths)

step_caroline = (maximum_caroline - minimum_caroline) / 10
smallstep_caroline = step_caroline / 10

step_us = (maximum_us - minimum_us) / 10
smallstep_us = step_us / 10

silvio_caroline = []
for i in range(10):
    silvio_caroline.append(maximum_caroline - (step_caroline * i))

tom_caroline = []
for i in range(10):
    tom_caroline.append(maximum_caroline - (smallstep_caroline * i))

silvio_us = []
for i in range(10):
    silvio_us.append(maximum_us - (step_us * i))

tom_us = []
for i in range(10):
    tom_us.append(maximum_us - (smallstep_us * i))


for value in a_list_of_streamline_lengths:
    for i in range(10):
        if value >= maximum_caroline - (step_caroline * (i+1)):
            distribution_caroline[i] += 1
            break

for value in a_list_of_streamline_lengths:
    for i in range(10):
        if value >= maximum_caroline - (smallstep_caroline * (i+1)):
            tenpercentdistribution_caroline[i] += 1
            break

for value in streamline_lengths:
    for i in range(10):
        if value >= maximum_us - (step_us * (i+1)):
            distribution_us[i] += 1
            break

for value in streamline_lengths:
    for i in range(10):
        if value >= maximum_us - (smallstep_us * (i+1)):
            tenpercentdistribution_us[i] += 1
            break

plt.subplot(4, 1, 1)
plt.bar(silvio_caroline, distribution_caroline)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution CAROLINE')

plt.subplot(4, 1, 2)
plt.bar(tom_caroline, tenpercentdistribution_caroline)
plt.xlabel('Fraction Within 10PC of Max Length', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution CAROLINE')

plt.subplot(4, 1, 3)
plt.bar(silvio_us, distribution_us)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution US')

plt.subplot(4, 1, 4)
plt.bar(tom_us, tenpercentdistribution_us)
plt.xlabel('Fraction Within 10PC of Max Length', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution US')

plt.show()