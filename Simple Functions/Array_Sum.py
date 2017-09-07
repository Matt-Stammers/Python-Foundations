# Simples, can be done several ways

import numpy as np

def sum_array(a):
	return np.sum(a)
  
# or simpler:

def sum_array(a):
  return sum(a)
  
# or
sum_array = sum

# or
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

# or even:
def sum_array(a):
    i = 0
    tot = 0
    while i < len(a):
        tot += a[i]
        i +=  1
    return tot
