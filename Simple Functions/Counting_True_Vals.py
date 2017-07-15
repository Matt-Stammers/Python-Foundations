# This can be achieved with numpy as below:

import numpy as np

def count_True(array):
    return np.count_nonzero(array)
    
# or without

def count_True(array):
    return array.count(True)
    
# or like this for the for loop in the counting_sheep variation:

def count_sheeps(array_of_sheep):
  # TODO May the force be with you
  count = 0
  for sheep in array_of_sheep:
      if sheep:
          count += 1 
  return count
 
# or as a list expression:

def count_sheeps(sheep):
  return len([x for x in sheep if x])
