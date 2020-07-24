import numpy as np



#indexing in array
# +ve as well as -ve use
a = np.array([1,2,3,4,5])
print(a)
print(a[1])
print(a[-1])
print(a[:3])
print(a[3:])
print(a[1:4])
print(a[:-2])
print(a[-3:-1])


a = np.array([[1,2,3],[4,5,6]])                     #2d array
print(a)
print(a[0][1])
print(a[-2][-2])
print(a[1])                                          #give 1st row


#3d array   i=no. of 2d array j= number of row k=no. of clm

a=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[11,2,3]]])   # 3d array
print(a)
print(a[0][1][1])
print(a[1][0][1])
