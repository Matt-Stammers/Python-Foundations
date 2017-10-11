# Say we wanted to multiply every single item in an array. We could accomplish this by using parenthesis but this would suck, so:

# next best is to iterate over the array:

def grow(arr):
  prod = 1
  for num in arr:
    prod = prod * num
  return prod
  
# fine for small jobs, but this is inefficient.
# why don't we try something else: This is better:

def grow(arr):
  product = 1
  for i in arr:
    product *= i
  return product
  
# but still inefficient as a new variable has to be assigned and this is computationally expensive. So we can use reduce:

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr) # this is a more efficient way to process the problem
    
# we can also use mul:

from functools import reduce
from operator import mul

def grow(arr):
    return reduce(mul, arr, 1)
