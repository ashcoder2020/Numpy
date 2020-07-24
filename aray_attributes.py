import numpy as np

#Attribute of array
#------------------------------------------------------------
#dimension
a = np.array([1,2,3])
print(a.ndim)                               #gives the dimension of given array

a = np.array([[1,2,3],[3,4,5]])
print(a.ndim)                               #gives the dimension of given array

# shape
a = np.array([[1,2],[1,2]])
print(a.shape)                              #give shape of array

a = np.array([[[1,2,3]]])                   #give 3 dimension shape
print(a.shape)  


#size                                       #total number of ele in array
print(a.size)
x = np.zeros((2,3,4))
print(x)
print(x.size)                              # total elements present array
print(x.shape)                             #shape
print(x.ndim)                              #dimension
print(x.dtype)                             #give datatype of element in array
print(x.itemsize)                          #tell size of each element in array

