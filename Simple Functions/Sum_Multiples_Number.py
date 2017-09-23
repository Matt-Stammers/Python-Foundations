# This function sums all the multiples of the numbers between two numbers using n as the stride length

def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
        
def sum_mul(n, m):
    return sum(x for x in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'
    
def sum_mul(n, m):
    sumu = 0
    if n > 0 and m > 0:
        for i in range(n, m):
            if (i % n == 0):
                sumu += i
    else:
        return 'INVALID'
    return sumu
    
def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    return sum([n*i for i in range(int(m/n) + 1) if n*i < m])
