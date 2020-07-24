import numpy as np

#linspace()                                               #evenly spaced value like arange()
x = np.linspace(0,100,num=5)                              #float type
print(x)
x = np.linspace(1,100,num=5,dtype='int')                  #int type
print(x)

x = np.linspace(1,100,num=5,endpoint=False)
print(x)

x = np.linspace(1,100,num=5,dtype='int', endpoint=False)  #dont include endpoint means 100 here
print(x)

x = np.linspace(1,100,num=5,dtype='int', retstep = True)  #give diffrence between each word
print(x)  
x = np.linspace(1,10)                                     #default num =50
print(x)
