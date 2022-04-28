import numpy as np
import scipy
#import compas
import plotly.graph_objects as go
import interpolation_primary #gives you the function interpolator(mesh, u_list, v_list, w_list, x, y, z, method)
from discrete_vector_field_generator import vector_field_ones
from interpolation_primary import mesh, array

#initation a uniform mesh of 10x10x10 points distributed on a space of xyz =10x10x10
mesh10_3 = np.vstack(np.meshgrid(np.arange(10),np.arange(10),np.arange(10))).reshape(3,-1).T

#uniform vector field of u,v,w = 1,1,1 defined at the mesh points of the mesh above
field_ones = np.ones((1000,3))

#choose field vector field to visualise
field = field_ones

#initialising streamtube plot
data = go.Streamtube(x=mesh10_3[:,0],y=mesh10_3[:,1],z=mesh10_3[:,2],u=field[:,0],v=field[:,1],w=field[:,2],starts = dict(x= [1,1],y= [9,1],z =[7,1]))
#visualising vector field

fig = go.Figure(data=data)


fig = go.Figure(data=go.Streamtube(
    x=mesh10_3[:,0],
    y=mesh10_3[:,1],
    z=mesh10_3[:,2],
    u=field[:,0],
    v=field[:,1],
    w=field[:,2],
    starts = dict(
        x= [1,1],
        y= [9,1],
        z =[7,1]
    )

))
"""
fig = go.Figure(data=go.Cone(x=mesh[:,0],y=mesh[:,1],z=mesh[:,2],u=array[:,0],v=array[:,1],w=array[:,2]))

"""
fig.show()












