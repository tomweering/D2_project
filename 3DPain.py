import numpy as np
import matplotlib.pyplot as plt

#make location arrays
x = np.arange(-47,47,1)
y = np.arange(-29,29,1)
z = np.arange(-18,18,1)

#load vector field data

vf = np.loadtxt('field_vect.csv', dtype=float, delimiter=",", skiprows=10, usecols=(0,1,2))
#
Ex = []
Ey = []
Ez = []
#
for j in range(35):
    ex = []
    ey = []
    ez = []
    for n in range(94):
        for i in range(58):
            ax, ay, az = vf[(n*59) + i + j*(95*59)]
            ex.append(ax)
            ey.append(ay)
            ez.append(az)

    Ex.append(ex)
    Ey.append(ey)
    Ez.append(ez)



# print(ex)

X,Y,Z = np.meshgrid(x,y,z, indexing='ij')

# Depict illustration
fig = plt.figure(figsize=(50, 50))

ax = plt.axes(projection = "3d")

ax.scatter3D(X, Y, Z)

plt.show()


#plt.quiver(Y,X,Ex,Ey)   #Coordinates are messed up
#
#plt.title('Electromagnetic Field')
#plt.grid()
#plt.show()



