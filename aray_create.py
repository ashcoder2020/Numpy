
import numpy as np

a = np.array([[1,2,3.3],[1,2,3],[1,2,3]],int,ndmin =2)              #2D aray
print("all ements in array are : ",a)
print(type(a))                                                      #shows the type of aray
print("devide all element by 2 :",a/2)                              #devide all elements in aray by 2
t = np.array((4,5,6,7,8))                                           #1D aray
print(t)
print(type(t))
l = list(t)                                                         #convert aray to list type
print(l)
print(type(l))