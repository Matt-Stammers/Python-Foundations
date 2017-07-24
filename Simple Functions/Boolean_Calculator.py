# One way to use boolean operators is these operators but they do not work element-wise in an array

from operator import xor
from operator import and_
from operator import or

def logical_calc(array, op):
    if op == "AND":
        return and_(array[0], array[1])
    elif op == "OR":
        return bool(array[0], array[1])
    elif op == "XOR":
        return xor(array[0], array[1])
        
# This way of using operator does work elementwise

import operator

OPS = {
    "AND": operator.and_,
    "OR" : operator.or_,
    "XOR": operator.xor
}

def logical_calc(array, op):
    return reduce(OPS[op], array)

# but much more powerful is numpy

import numpy as np - 

# the array can be reduced to 1 element using .reduce 

def logical_calc(array, op):
    if op == "AND":
        return np.logical_and.reduce(np.array(array))
    elif op == "OR":
        return np.logical_or.reduce(np.array(array))
    elif op == "XOR":
        return np.logical_xor.reduce(np.array(array))
        
# another way

def logical_calc(array, op):
    ops = {
            "AND" : lambda x,y: x & y,
            "OR"  : lambda x,y: x | y,
            "XOR" : lambda x,y: x ^ y
           }
  
    from functools import reduce
    return reduce(ops[op], array)
