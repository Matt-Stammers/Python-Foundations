# This can be done like this:

def print_array(arr):
  return ','.join(str(a) for a in arr)
  
# or by using .map:

def print_array(arr):
    return ','.join(map(str, arr))
    
# all the other ways are weaker.
