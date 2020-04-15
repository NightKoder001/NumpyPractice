import numpy as np
from numpy import random
"""Generate Random Number"""
#NumPy offers the random module to work with random numbers.
#Generate a random integer from 0 to 100:
x = random.randint(100)
print(x) 


"""Generate Random Float """
#The random module's rand() method returns a random float between 0 and 1.
#Generate a random float from 0 to 1:
x = random.rand()
print(x)


"""Generate Random Array """
#In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.
#Integers-The randint() method takes a size parameter where you can specify the shape of an array.

#Generate a 1-D array containing 5 random integers from 0 to 100:
x=random.randint(100, size=(5))
print(x) 

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.randint(100, size=(3, 5))
print(x) 

#Floats-The rand() method also allows you to specify the shape of the array.
#Generate a 1-D array containing 5 random floats:
x = random.rand(5)
print(x) 

#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x = random.rand(3, 5)
print(x) 







 