# Say you had two 3 integer arrays and you looked to cube them and find the difference. One way to complete that challenge would be:

def find_difference(a, b):
    cube_a = a[0]*a[1]*a[2]
    cube_b = b[0]*b[1]*b[2]
    return abs(cube_a - cube_b)
    
# less readable but more compact

def find_difference(a, b):
  
return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])
    
# Or you could use numpy and prod

from numpy import prod

def find_difference(a, b):
    return abs(prod(a) - prod(b))

#abs returns the absolute difference to make sure that the results are not positive and negative.

# another option is to use some other operators:

from functools import reduce as r
from operator import mul, sub

def find_difference(a, b):
    return abs(r(sub, [r(mul, a), r(mul, b)]))
    
    # or
    
from functools import reduce as r
from operator import mul, sub

def find_difference(a, b):
    return abs(r(sub, [r(mul, a), r(mul, b)]))
    
# You can also use zip to perform a similar operation but this is definitely not the best way to do it

def find_difference(a, b):
    A = B = 1
    for i, j in zip(a, b):
        A *= i
        B *= j
    return abs(A - B)
