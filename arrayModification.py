#__________Insert Array_______
#1d
import numpy as np
num = np.array([1,3,4,5,6])
#print(np.insert(num ,3,49,axis=0))

#2d
arr1 = np.array([[1, 2, 3],[3,3,3]])
arr2 = np.insert(arr1, 0 , [3,4,3] , axis=0)
#print(arr2)

#_________Append__________
num = np.array([1,3,4,5,6 , 8, 8])
#print(np.append(num, 3))

#_________Concatenate__________
array1 = np.array([10,20,20])
array2 = np.array([90,50,44])
newArray = np.concatenate((array1 , array2))
#print(newArray)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
#print(arr)
#_________________NOTE__________________:
#axis=0 --> Horizontal and axis=1 ---> Vertical
#The main difference between append and insert method is, append is used to add something at the end of array while insert method is use to add something on a specific place in array {it may be  in start , center, (or may be at end like append)}

#_________delete__________
array1 = np.array([[10,20,20],[33,23,12]])
new_arr= np.delete(array1,1,axis=0)
#print(new_arr)

#____________Split________
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)
print(new_arr[1])