# This is based on the collaz collective - a tricky mathematical problem.

def hotpo(n):
    iterations = 0
    while n != 1:
        (n*3)+1 if n%2 else n/2
        iterations += 1
    return iterations
    
def hotpo(n):
    cnt = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        cnt += 1
    return cnt
