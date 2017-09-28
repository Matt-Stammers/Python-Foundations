# this 'hack' will get you some way, but won't handle all exclusions:

def paperwork(n, m):
    if n + m > 1:
        return abs(n * m)
    else:
        return 0
        
# this handling system is much better: 

def paperwork(n, m):
    if m<0 or n<0:
        return 0
    else:
        return n*m
        
# it can be abbreviated to:

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

# or you can do the following:

def paperwork(n, m):
    return max(n, 0)*max(m, 0)
    
paperwork = lambda n, m: n.__mul__(m) if n >= 0 and m >= 0 else 0
