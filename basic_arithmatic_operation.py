import numpy as np



#arithmatic operation on array
a= np.array([1,2,3,4,5,6])
print(a)
print(a*2)
print(a-1)
print(a/2)
print(a%2)
print(a+2)

a = np.zeros((3,3))                 #2d array
print(a)
print(a+2)
print(a*7)
print(a/4)



#operation on two arrays                #contain same shape
a=np.arange(1,5)
b = np.arange(11,15)
print(a)
print(b)
print(a+b)                              #add same index elements in two arrays
print(a-b) 
print(a/b) 
print(a*b) 



#2d array arithmatic
a = np.eye(2,3,dtype='int')
print(a)
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))

