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

def hotpo(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

# or as a double function call:

def hotpo(n):
    def even_odd(m):
        return [3*m+1, m/2][m%2==0]
    c = 0
    while n!=1:
        n =  even_odd(n)
        c+=1
    return c

# or using lots of abbreviations:

def hotpo(n):
    t = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
        t += 1
    return t

# or as a crazy one liner

def hotpo(num, count=0):
    return count if num == 1 else hotpo(num / 2 if num % 2 == 0 else num * 3 + 1 ,count + 1)

# the increment can go before or after the filters

def hotpo(n):
    c = 0
    while n != 1:
        c += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1

    return c

# this is a slightly crazy way to do it but it works

def hotpo(n):
    if n == 1:
        return 0
    else:
        return 1 + (hotpo(n * 3 + 1) if n % 2 else hotpo(int(n / 2)))
    
# or as a lambda:

hotpo = lambda n: 1 + hotpo(int(n / 2) if n % 2 == 0 else 3 * n + 1) if n > 1 else 0

# or a really interesting way using memoization

def hotpo(start, memo={2: 1}):
    """ uses memoization """
    n = start
    seq_l = 0
    while n > 1:
        if memo.get(n, False):
            if n != start:
                memo[start] = memo[n] + seq_l
            return memo[n] + seq_l
        if n % 2 == 0:
            n = n // 2
            seq_l += 1
        else:
            n = (n * 3 + 1) // 2  # returns even value so -> // 2 skip's it.
            seq_l += 2
    return 0
