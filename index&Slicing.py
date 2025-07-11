#________Indexing________ 1d
import numpy as np
number = np.array([1,2,3,4])
#print(number[3])
#print(number[-1])
#print(number[0])


#2d
number = np.array([[4,5,6,3],[2,4,5,9]])
#print(number[0,3])
#print(number[1,1])

#MultiDimensional:
number = np.array([[[1,2,3],[3,5,6]],[[7,6,5],[7,8,9]]])
#print(number[0,1,1]) 
#print(number[1,0,2]) 

#Negative 
number = np.array([40,50,44,33])
#print(number[-2])


#________Slicing________
#print(number[:2])
#print(number[0:4:2])
#print(number[::-1]) #For reserve array