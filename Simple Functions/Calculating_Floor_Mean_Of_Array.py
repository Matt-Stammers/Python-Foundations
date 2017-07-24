# this is a hacky way to solve this problem and get the mean

def get_average(marks):
    return sum(marks) / len(marks)
    
def get_average(marks):
    average = sum(marks) / len(marks)    
    return int(average)
    
# int will also round down by default.
       
# using math and numpy
    
import numpy as np
import math

def get_average(marks):
    return math.floor(np.mean(marks))
    raise NotImplementedError("TODO: get_average")
    
# or

import numpy

def get_average(marks):
    return int(numpy.mean(marks))
