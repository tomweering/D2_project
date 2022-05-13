import matplotlib.pyplot as plt
import numpy as np

print("The AVERAGE streamline lenght is", np.average(list_of_streamlines), "mm")
print("The LONGEST streamline lenght is", max(streamline_lengths), "mm")
print("The SHORTEST streamline lenght is", min(streamlines_lengths), "mm")

streamline_lengths = [78, 94, 28, 57, 48, 89, 91, 47, 47, 84, 55]
distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
maximum = max(streamline_lengths)
minimum = min(streamline_lengths)
step = (maximum - minimum) / 10
silvio = []
for i in range(10):
    silvio.append(maximum - (step * i))
print(silvio)
for value in streamline_lengths:
    for i in range(10):
        if value >= maximum - (step * (i+1)):
            distribution[i] += 1
            break



plt.bar(silvio, distribution)
plt.xlabel('Fraction Of Max Length Streamline', fontsize=5)
plt.ylabel('# of Streamlines', fontsize=5)
plt.title('Streamline Length Distribution')
plt.show()
