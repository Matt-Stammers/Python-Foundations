# as below

def count_by(x, n):
    """
    Returns a sequence of numbers counting by `x` `n` times.
    """
    return [i*x for i in range(1,n+1)]
    
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return range(x, x * n + 1, x)
    
# much easier to do this as a list experession but it can be done using for or while as well:

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    output = []
    i = 1
    while len(output) < n:
        output.append(i*x)
        i += 1
    return output
    
def count_by(x, n):
    mult = []
    for i in range(1, n+1):
        mult.append(x*i)
    return mult
