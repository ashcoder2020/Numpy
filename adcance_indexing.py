import numpy as np


#2d array   array within array
a = np.array([[1,2],[3,4],[5,6]])           #a[start:end:step,start:end:step]   1st start end step is for row and second for column
print(a)
print(a[1:,1:])                             #slice 1st row 1st clm
print(a[0:2,0:1])
print(a[:,:])                               #print entire array
