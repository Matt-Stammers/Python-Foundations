# convert a digit to a list and reverse it:

def digitize(n):
    n = str(n)
    s = n[::-1]
    print(s)
    return [int(d) for d in str(s)]
    
# very clever way to do it

def digitize(n):
    return map(int, str(n)[::-1])
    
# with a list expression    
    
def digitize(n):
    return [int(x) for x in str(n)[::-1]]
    
# using reverse:

def digitize(n):
    return [int(x) for x in reversed(str(n))]
    
# another variation using while.

def digitize(n):
    result = []
    while n >= 1:
        result.append(n%10)
        n //= 10
    return result
