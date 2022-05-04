import numpy as np



def scaled_vector_processing(datafile):
    #process a csv file formed of scaled vectors associated with a mesh to return an array of unit vectors with a single scalar value describing the scaling
    with open(datafile) as f:
        array = np.loadtxt(f,delimiter=",")

    scalars = np.linalg.norm(array,axis=1)
    direction_vectors = (array.T/scalars).T
    print(scalars)
    return direction_vectors, scalars

direction_vectors, scalars = scaled_vector_processing("output_vfield.csv")
        
    
