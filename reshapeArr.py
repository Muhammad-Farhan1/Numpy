import numpy as np
number = np.array([1,2,3,4,5,6])
#print(number.reshape(2,3))

num2d = np.array([[4,5,6,3],[2,4,5,9]])
#print(num2d.reshape(-1))
#print(num2d.ravel()) #it returns "view"
#print(num2d.flatten()) #it returns "copy"

#1-d to 3-d:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.reshape(2, 3, 2))