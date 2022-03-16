import numpy as np
import matplotlib.pyplot as plt


#ax = plt.figure().add_subplot(projection='3d')
#make location arrays
x = np.arange(-32,32,1)
y = np.arange(-8,8,1)


#load vector field data

#getting data from CSV file
with open("filtered_2D.csv") as f:
    array_CSV = np.loadtxt(f, delimiter=",")

Ex = array_CSV[:,:16]
Ey = array_CSV[:,16:]


X,Y = np.meshgrid(x,y)

# Depict illustration
#fig = plt.figure(figsize=(50, 50))

#ax = plt.axes(projection = "3d")
#ax.scatter3D(X, Y, Z)
#ax.quiver(X, Y, Ex, Ey, length=0.01, normalize=True)
#plt.show()


plt.quiver(X,Y,Ex,Ey)   #Coordinates are messed up
#
#plt.title('Electromagnetic Field')
plt.grid()
plt.show()



