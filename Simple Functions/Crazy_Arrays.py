# this program returns True if a array is larger than b array.

def array_madness(a,b):
    a_sum = sum([x**2 for x in a])
    b_sum = sum([x**3 for x in b])
    if a_sum > b_sum:
    	return True
    else:
    	return False

def array_madness(a,b):
    return sum(x ** 2 for x in a) > sum(x **3 for x in b)
    
def array_madness(a,b):
    return True if sum(x**2 for x in a) > sum(x**3 for x in b) else False
    
def array_madness(a,b):
    return sum(map(lambda s: s**2, a)) > sum(map(lambda s: s**3, b))
