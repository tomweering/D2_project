
# LIST is list of streamline lenghts
import numpy as np
from matplotlib import pyplot as plt

printarea = 0.1 #mm^2
print("The AVERAGE streamline lenght is", np.average(list_of_streamlines), "mm")
print("The LONGEST streamline lenght is", max(list_of_streamlines), "mm")
print("The SHORTEST streamline lenght is", min(list_of_streamlines), "mm")

