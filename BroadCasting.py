
import numpy as np
array1 = np.array([10,20,30])
array2 = np.array([3])
multiply = array1 * array2
#print(multiply)

#2D
arr1 = np.array([[5,5,5],[2,3,4]])
arr2 = np.array([2,3,4])
add = arr1 + arr2
#print(add)

#Wrong MEthod 
ar1 = np.array([[3,4,5],[2,2,2]])
ar2 = np.array([2,3])
add = ar1 + ar2
#print(add)

#(e.g., arr1 + arr2)---> Vectorization
#(e.g., arr + 5)---> Broadcasting