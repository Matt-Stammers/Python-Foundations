# Removing the min and max values from an array then returning the sum of the remaining values.

def sum_array(arr): # removes outliers and handles tiny arrays
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

def sum_array(arr): # another way of doing it
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

def sum_array(arr):
    if arr==None or len(arr)==0 or len(arr)==1:return 0
    return (sum(arr)-max(arr)-min(arr))

def sum_array(arr):
    if arr == [] or arr == None or len(arr) == 1:
        return 0
    else:
        return (- (max(arr) + min(arr)) + sum(arr))
