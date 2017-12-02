# This formula will return true if an int is a perfect square:

from math import sqrt

def is_square(n):    
  return n > 0 and sqrt(n).is_integer()
  
# simples.
