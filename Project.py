#In this project , i will calculate the mean, median, mode on students marks

import numpy as np
from scipy import stats

marks = np.array([80, 98, 44, 89, 37, 80 , 90, 54])

def analyze_marks(marks):
    mean = np.mean(marks)
    median = np.median(marks)
    mode = stats.mode(marks)
    std = np.std(marks)

    print(f"The mean of students marks is {mean:.2f}")
    print(f"The median of students marks is {median}")
    print(f"The mode of students marks is {mode.mode} (appears {mode.count} times)")
    print(f"The standard deviation of students marks is {std:.2f}")

    print("-----Performance of Class-----")
    if mean > 75:
        print("Class performance is Good!")
    elif 50 < mean <= 75:    
        print("Class Performance is Average!")
    else:
        print("Class Performance is not Good!")   
       
analyze_marks(marks)