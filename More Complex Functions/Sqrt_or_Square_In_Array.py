# This function returns perfect square roots only, otherwise it squares all the other numbers:

def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result

# this is another way to do it using moduleo instead

from math import sqrt

def square_or_square_root(arr):
    return [int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr]
    
# using numpy

import numpy as np
def square_or_square_root(arr):
    newarray = []
    for number in arr:
        if (np.sqrt(number)).is_integer(): #checks if the number has numbers after the decimal point by determining if its a float
            newarray.append(np.sqrt(number))
        else: 
            newarray.append(number*number)
    return newarray
