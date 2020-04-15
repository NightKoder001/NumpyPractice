import numpy as np
from numpy import random
"""Generate Random Number From Array
The choice() method allows you to generate a random value based on an array of values.
The choice() method takes an array as a parameter and randomly returns one of the values. """

#Return one of the values in an array:
x = random.choice([3, 5, 7, 9])
print(x) 
#The choice() method also allows you to return an array of values.
#Add a size parameter to specify the shape of the array.


#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x) 

 