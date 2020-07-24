import numpy as np


#zeroes()
#help(np.zeros)  
x = np.zeros(5)                                               # default float type data one dimesion whith 5 element     
print(x)
x = np.zeros(3,dtype='int')                                   #array type int
print(x)
x = np.zeros((2,3), dtype='int')                              #2 row 3 column 2D aray
print(x)
x = np.zeros([3,3])                                           #3 row 3 clm
print(x)
x = np.array([[1,2,3],[4,5,6],[7,8,9]],order="F")
print(x)
