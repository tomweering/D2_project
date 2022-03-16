import numpy as np
import matplotlib.pyplot as plt

#make location arrays
y = np.arange(-32,32,1)
x = np.arange(-8,8,1)

#load vector field data

vf = np.loadtxt('vectorField.csv', dtype=float, delimiter=",", skiprows=10, usecols=(1,2))

Ex = []
Ey = []


for n in range(64):
    ex = []
    ey = []
    for i in range(16):
        ax, ay = vf[(n*16) + i]
        ex.append(ax)
        ey.append(ay)

    Ex.append(ex)
    Ey.append(ey)


X,Y = np.meshgrid(x,y)

# Depict illustration
plt.figure(figsize=(100, 100))
plt.quiver(Y,X,Ex,Ey)   #Coordinates are messed up


plt.grid()
plt.show()