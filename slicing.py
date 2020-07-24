import numpy as np


# slicing  indexing start from zero
a  = np.array([7,3,4,5,2,1,6,0])
print(a)
print(a[2:5:2])                                 #start end step
print(a[1])
print(a[-1])
print(a[:3])
print(a[3:])
print(a[1:4])
print(a[:-2])
print(a[-3:-1])



#2d array   array within array
a = np.array([[1,2],[3,4],[5,6]])              #a[start:end:step,start:end:step]   1st start end step is for row and second for column
print(a)
print(a[1:,1:])                                #slice 1st row 1st clm
print(a[0:2,0:1])
print(a[:,:])                                  #print entire array
