import numpy as np

x = np.arange(-5, 5, 2)
y = np.arange(-4, 4, 2)
xx, yy = np.meshgrid(x, y)
data = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)

print(data)  # In meshgrid format
