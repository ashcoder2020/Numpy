
#operation on diffremt size array or shape     
#broadcasting rules
#size of each dimension should same
#size of one of the dimension should 1






import numpy as np

#reshaping array    #np.shape(array,shape,order)    not change data
a = np.arange(0,10)
print(a)
print(a.shape)
b = np.reshape(a,(5,2))                            #change(1d array to 5*2 )
print(b)

c = np.reshape(a,(5,2), order='F')                 #f = columnwise    C= row wise
print(c)
print(a.size)                                      #number of element present in array
print(c.size)

print(a.shape)
print(c.shape)
print(a.reshape(2,5))                              #easy method 





#resize                 change size and total values in array      np.resize(array_name,shape)
a = np.arange(0,10)
print(a)
a = np.resize(a,(5,3))                             #after end value then it repeat the values
print(a)





#flatening numpy arrays
a = np.zeros((3,3),dtype='int')
print(a)
print(a.flatten())                                  #convert n dimension array to one dimension array

print(a.ravel())                                    #convert one dimension array

print(a)

