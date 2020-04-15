import numpy as np
#Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) 
print(x) 

#Make a view, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr) 
print(x) 

#Make a view, change the view, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr) 
print(x) 

"""
Check if Array Owns it's Data
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object. 
"""
#Print the value of the base attribute to check if an array owns it's data or not:
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#Print the value of the base attribute to check if an array owns it's data or not:
