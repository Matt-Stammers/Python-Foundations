# remove top and bottom values and return the rest (various ways to do it) 

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
    
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0
    
def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])
    
def sum_array(arr):
    return sum(arr) - min(arr) - max(arr) if arr and len(arr) > 1 else 0
  
