import matplotlib.pyplot as plt
import numpy as np

print("The AVERAGE streamline lenght is", np.average(a_list_of_streamline_lengths), "mm")
print("The LONGEST streamline lenght is", max(a_list_of_streamline_lengths), "mm")
print("The SHORTEST streamline lenght is", min(a_list_of_streamline_lengths), "mm")

distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tenpercentdistribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
maximum = max(a_list_of_streamline_lengths)
minimum = min(a_list_of_streamline_lengths)
step = (maximum - minimum) / 10
smallstep = step / 10

silvio = []
for i in range(10):
    silvio.append(maximum - (step * i))

tom = []
for i in range(10):
    tom.append(maximum - (smallstep * i))

for value in a_list_of_streamline_lengths:
    for i in range(10):
        if value >= maximum - (step * (i+1)):
            distribution[i] += 1
            break

for value in a_list_of_streamline_lengths:
    for i in range(10):
        if value >= maximum - (smallstep * (i+1)):
            tenpercentdistribution[i] += 1
            break

plt.subplot(2, 1, 1)
plt.bar(silvio, distribution)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution')

plt.subplot(2, 1, 2)
plt.bar(tom, tenpercentdistribution)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=10)
plt.ylabel('# of Streamlines', fontsize=10)
plt.title('Streamline Length Distribution')

plt.show()
