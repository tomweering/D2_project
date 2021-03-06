#functions for generating vector field and filtering out vectors of small magnitude (norm less than a specified value)
from logging import NullHandler
import numpy as np
import matplotlib.pyplot as plt
import csv

from pyparsing import null_debug_action

def filter2D(vector_field, norm_criteria):
    vf = np.loadtxt(vector_field, dtype=float, delimiter=",", skiprows=10, usecols=(1,2))
    Ex = []
    Ey = []
    for n in range(64):
        ex = []
        ey = []
        for i in range(16):
            ax, ay,  = vf[(n*16) + i]
            if np.sqrt(ax**2+ay**2) < norm_criteria:
                ex.append(0)
                ey.append(0)
            else:
                ex.append(ax)
                ey.append(ay)
        Ex.append(ex)
        Ey.append(ey)
    array = np.concatenate((Ex, Ey), axis=1)
    with open("filtered_2D.csv","w+",newline='') as f:
        csvWriter = csv.writer(f,delimiter=',')
        csvWriter.writerows(array)
    return array

def filter3D(vector_field, norm_criteria):
    return null



#filter2D('vectorField_scaledByDensity.csv', 0.1)