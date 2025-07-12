#Mean - The average value
#Median - The mid point value(Middle value)
#Mode - The most common value(most number of times)
#Standard Deviation - std()

#-----Mean-----
#it works like -> (120+124+220+80+48+189+200)/7 == 140.14285714285714
import numpy as np
speed_of_cars = np.array([120,124,220,80,48,189,200])
mean = np.mean(speed_of_cars)
#print(f"{mean:.2f}")


#-----Median----
#it works as -> len(nums) // 2 = 7 (7 is the index of nums value that is 4!)
nums = np.array([1,3,5,3,2,5,6,7,8,3,4,1,7,9,0])
median = np.median(nums)
#print(median)

#-----Mode-----
from scipy import stats
marks = np.array([12,14,11,11,10,14,11,9,8,12,12,11,14,15])
mod = stats.mode(marks)
print(mod)


#---Standard Deviation---
#formula -> σ = √[ Σ (xᵢ - μ)² / N ]
numbers = np.array([1,2,4,3,4,8,9])
std = np.std(numbers)
print(std)