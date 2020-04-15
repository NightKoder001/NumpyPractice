"""
NumPy is a python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
In Python we have lists that serve the purpose of arrays, but they are slow to process. NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently. This behavior is called locality of reference in computer science
"""

#Dimensions in Arrays
#A dimension in arrays is one level of array depth (nested arrays).
#nested array: are arrays that have arrays as their elements.



import numpy as np 
arr = np.array([1, 2, 3, 4, 5]) 
print(arr)


"""Check Number of Dimensions"""
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
#Check how many dimensions the arrays have:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) 
print(b.ndim) 
print(c.ndim) 
print(d.ndim)

""" Higher dimensional arrays"""
#An array can have any number of dimensions.
#When the array is created, you can define the number of dimensions by using the ndmin argument.
#Create an array with 5 dimensions and verify that it has 5 dimensions:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim) 
""" 
In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
"""

""" 3-D arrays """
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
#These are often used to represent a 3rd order tensor.
#Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr) 


""" 2-D Arrays """
#An array that has 1-D arrays as its elements is called a 2-D array.
#These are often used to represent matrix or 2nd order tensors.
#NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr) 

"""1-D Array"""
#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
#Create a 1-D array containing the values 1,2,3,4,5:
arr = np.array([1, 2, 3, 4, 5])

print(arr) 


""" 0-D Arrays """
#0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
#Create a 0-D array with value 42
arr = np.array(42)

print(arr)