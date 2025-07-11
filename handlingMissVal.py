#isnan
#nan-to-num
#isinf

#------isnan------
import numpy as np
arr = np.array([1, 2 , 3 ,np.nan , 4 , np.nan])
#print(arr)
#print(np.isnan(arr))

#---nam-to-num---
arr = np.array([1 , np.nan , 3 , 5])
#print(arr)
valued_arr = np.nan_to_num(arr , nan=100)
#print(valued_arr)

#---isinf---
array = np.array([1 , 3  , np.inf , -np.inf])
print(array)
value_arr = np.nan_to_num(array , posinf=100 , neginf=-20)
print(value_arr)