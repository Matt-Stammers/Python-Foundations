from math import factorial
from math import sqrt

def isPrime(n):
    if n <= 1:
        return False
    elif n in (2,3):
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i == 0: return False
        return True

def am_i_wilson(n):
    if isinstance(n,int) and isPrime(n):
        return (factorial(n-1) + 1) % n**2 == 0
    else:
        return False
