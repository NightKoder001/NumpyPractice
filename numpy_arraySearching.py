import numpy as np
"""Searching Arrays """
#You can search an array for a certain value, and return the indexes that get a match.To search an array, use the where() method.
#Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
#The example above will return a tuple: (array([3, 5, 6],)
#Which means that the value 4 is present at index 3, 5, and 6.

 
#Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x) 


#Find the indexes where the values are odd:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x) 