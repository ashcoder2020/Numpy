import numpy as np

#Eye()                              #set diagonal values       
x = np.eye(5)                       #draw 5*5 diagonal matrix
print(x)
x = np.eye(2,3)                     #2 row 3 column with diagonal matrix
print(x)

x = np.eye(4,k=-1)                  #lower diagonal 1 is -ve index k=-ve
print(x)
x = np.eye(4,k=1)                   #upper diagonal 1 is +ve index k=+ve
print(x)
x = np.identity(4)                  #return identity matrix 4*4
print(x)
