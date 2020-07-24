import numpy as np

#boolean indexing
x= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print(x[x<7])                   #give all element less than 7 here co0ndition pass in index
print(x[x>8]*2)                 #condition uised here

