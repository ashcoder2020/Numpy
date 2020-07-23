import numpy as np
"""

#How to create array
#----------------------------------------------------
# array()
a = np.array([[1,2,3.3],[1,2,3],[1,2,3]],int,ndmin =2)
print("all ements in array are : ",a)
print(type(a))
print("devide all element by 2 :",a/2)
t = np.array((4,5,6,7,8))
print(t)
print(type(t))
l = list(t)
print(l)
print(type(l))



#arange()
x = np.arange(1,15)
print(x)
x = np.arange(5)
print(x)
x = np.arange(1,10,2)
print(x)
x = np.arange(5,9,2,dtype=float)
print(x)





#zeroes()
#help(np.zeros)  
x = np.zeros(5)             # default float type data one dimesion whith 5 element     
print(x)
x = np.zeros(3,dtype='int')         #array type int
print(x)
x = np.zeros((2,3), dtype='int')                 #2 row 3 column
print(x)
x = np.zeros([3,3])          #3 row 3 clm
print(x)
x = np.array([[1,2,3],[4,5,6],[7,8,9]],order="F")
print(x)





#ones()             #create array filled with ones
x= np.ones(5)
print(x)
x= np.ones(4,dtype='int')
print(x)
x = np.ones((3,4))              #3 row 4 clm
print(x)








#empty()
x = np.empty(4)                         #create random value aray of 4 element
print(x)
x= np.empty((4,4),dtype='int')
print(x)







#linspace()                 #evenly spaced value like arange()
x = np.linspace(0,100,num=5)                #float type
print(x)
x = np.linspace(1,100,num=5,dtype='int')        #int type
print(x)

x = np.linspace(1,100,num=5,endpoint=False)
print(x)

x = np.linspace(1,100,num=5,dtype='int', endpoint=False)                #dont include endpoint means 100 here
print(x)

x = np.linspace(1,100,num=5,dtype='int', retstep = True)        #give diffrence between each word
print(x)  
x = np.linspace(1,10)                       #default num =50
print(x)







#Eye()                      #set diagonal values       
x = np.eye(5)               #draw 5*5 diagonal matrix
print(x)
x = np.eye(2,3)             #2 row 3 column with diagonal matrix
print(x)

x = np.eye(4,k=-1)                  #lower diagonal 1 is -ve index k=-ve
print(x)
x = np.eye(4,k=1)                  #upper diagonal 1 is +ve index k=+ve
print(x)
x = np.identity(4)                  #return identity matrix 4*4
print(x)








#random()                   #random number generation
x = np.random.rand(5)               #gives random values
print(x)
x = np.random.rand(5,4)             #5*4 array random value
print(x)
x = np.random.randint(3,4)              #r<c always
print(x)






#Attribute of array
#------------------------------------------------------------
#dimension
a = np.array([1,2,3])
print(a.ndim)                       #gives the dimension of given array

a = np.array([[1,2,3],[3,4,5]])
print(a.ndim)                            #gives the dimension of given array

# shape
a = np.array([[1,2],[1,2]])
print(a.shape)                  #give shape of array

a = np.array([[[1,2,3]]])               #give 3 dimension shape
print(a.shape)


#size               #total number of ele in array
print(a.size)
x = np.zeros((2,3,4))
print(x)
print(x.size)               # total elements present array
print(x.shape)          #shape
print(x.ndim)               #dimension
print(x.dtype)              #give datatype of element in array
print(x.itemsize)               #tell size of each element in array








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


a = np.array([[1,2,3],[4,5,6]])     #2d array
print(a)
print(a[0][1])
print(a[-2][-2])
print(a[1])                 #give 1st row


#3d array   i=no. of 2d array j= number of row k=no. of clm

a=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[11,2,3]]])          # 3d array
print(a)
print(a[0][1][1])
print(a[1][0][1])








# slicing  indexing start from zero
a  = np.array([7,3,4,5,2,1,6,0])
print(a)
print(a[2:5:2])             #start end step
print(a[1])
print(a[-1])
print(a[:3])
print(a[3:])
print(a[1:4])
print(a[:-2])
print(a[-3:-1])



#2d array   array within array
a = np.array([[1,2],[3,4],[5,6]])           #a[start:end:step,start:end:step]   1st start end step is for row and second for column
print(a)
print(a[1:,1:])                 #slice 1st row 1st clm
print(a[0:2,0:1])
print(a[:,:])                   #print entire array







#advance indexing                       #repeated also access

x = np.arange(1,10)             #create array of 9 element
print(x)
index = np.array([1,4,5])              #create new array for indexing option
print(x[[1,4,5]])
print(x[index])                         #pass index array as a index of original ray






#boolean indexing
x= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print(x[x<7])                   #give all element less than 7 here co0ndition pass in index
print(x[x>8]*2)                 #condition uised here





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
print(a+b)                  #add same index elements in two arrays
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






#operation on diffremt size array or shape     
 #broadcasting rules
#size of each dimension should same
#size of one of the dimension should 1








#reshaping array    #np.shape(array,shape,order)    not change data
a = np.arange(0,10)
print(a)
print(a.shape)
b = np.reshape(a,(5,2))                 #change(1d array to 5*2 )
print(b)

c = np.reshape(a,(5,2), order='F')              #f = columnwise    C= row wise
print(c)
print(a.size)               #number of element present in array
print(c.size)

print(a.shape)
print(c.shape)
print(a.reshape(2,5))               #easy method 





#resize                 change size and total values in array      np.resize(array_name,shape)
a = np.arange(0,10)
print(a)
a = np.resize(a,(5,3))                  #after end value then it repeat the values
print(a)





#flatening numpy arrays
a = np.zeros((3,3),dtype='int')
print(a)
print(a.flatten())               #convert n dimension array to one dimension array

print(a.ravel())                    #convert one dimension array

print(a)



"""















