# Removing the min and max values from an array then returning the sum of the remaining values.

def sum_array(arr): # removes outliers and handles tiny arrays
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
