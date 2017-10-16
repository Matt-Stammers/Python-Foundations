# say we wanted to identify all the numbers in a list that do not share any greatest common divisor other than 1. We can use gcd for this:

from fractions import gcd

def relatively_prime (n, l):
    return [x for x in l if gcd(n, x) == 1]
    
# it can be done without but it is very clunky:

def relatively_prime (n, l):
    print(n,l)
    A=set()
    for i in range(2,n+1):
        while n%i==0:
            A.add(i)
            n//=i
            
    B=[]
    for x in l:
        for i in A:
            if x%i==0:break 
        else:B.append(x)
    return B
