# This is based on the collaz collective

def hotpo(n):
    count = 0
    if n == 1:
        return count
    else:
        while n % 2 == 0:
            count =+ count
            return n/2
        while n % 2 == 1:
            count =+ count
            return (n*3)+1
    
