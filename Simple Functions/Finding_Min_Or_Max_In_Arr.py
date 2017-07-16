# find min and max in array

import numpy as np

def min(arr):
    return np.min(arr)

def max(arr):
    return np.max(arr)
    
def m(arr):
    return min(arr)

def m(arr):
    return max(arr)
    
def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high
    
def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]
