# This is a really simple function and it shouldn't cause too many issues but there are many ways to implement it.

the simplest way to do it is by using numpy.

import numpy as np
def find_average(array):
    return np.mean(array)
  
# or you can do:
 
def find_average(array):
    return sum(array) / len(array) if array else 0
  
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0
        
def find_average(array):
    if len(array) != 0:
        return sum(array) / len(array)
    else:
        return 0
        
find_average = lambda array: sum(array) / len(array) if array else 0
        
# This is a really crazy way to do it using OOP:

def find_average(array):
    if not array:
        return 0

    class SafeFloat(object):
        def __init__(self, val):
            super(SafeFloat, self).__init__()
            self.val = val

        def __eq__(self, float_val):
            # let me fix your comparisons..
            def isclose(a, b):
                return abs(a - b) < 0.00000001
            return isclose(self.val, float_val)

        def __str__(self):
            return str(self.val)

    from numpy import mean
    return SafeFloat(mean(array))
