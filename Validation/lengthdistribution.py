import matplotlib.pyplot as plt
import numpy as np
from validation import a_list_of_streamline_lengths, print_lines

print(type(print_lines))


print("The AVERAGE CAROLINE streamline lenght is", np.average(a_list_of_streamline_lengths), "mm")
print("The LONGEST CAROLINE streamline lenght is", max(a_list_of_streamline_lengths), "mm")
print("The SHORTEST CAROLINE streamline lenght is", min(a_list_of_streamline_lengths), "mm")

print("The AVERAGE streamline lenght is", np.average(print_lines), "mm") 
print("The LONGEST streamline lenght is", max(print_lines), "mm")
print("The SHORTEST streamline lenght is", min(print_lines), "mm")

distribution_caroline = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tenpercentdistribution_caroline = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

distribution_us = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tenpercentdistribution_us = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

maximum_caroline = max(a_list_of_streamline_lengths)
minimum_caroline = min(a_list_of_streamline_lengths)

maximum_us = max(print_lines)
minimum_us = min(print_lines)

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

for value in print_lines:
    for i in range(10):
        if value >= maximum_us - (step_us * (i+1)):
            distribution_us[i] += 1
            break

for value in print_lines:
    for i in range(10):
        if value >= maximum_us - (smallstep_us * (i+1)):
            tenpercentdistribution_us[i] += 1
            break

plt.subplot(4, 1, 1)
plt.bar(silvio_caroline, distribution_caroline)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution')

plt.subplot(4, 1, 2)
plt.bar(tom_caroline, tenpercentdistribution_caroline)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution')

plt.subplot(4, 1, 1)
plt.bar(silvio_us, distribution_us)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution')

plt.subplot(4, 1, 2)
plt.bar(tom_us, tenpercentdistribution_us)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution')

plt.show()
