# different ways to convert a list and then sum the values:

# the best way is the following:

def sum_mix(arr):
    return sum(map(int, arr))

def sum_mix(arr):
    result = 0
    for a in arr:
        try:
            result += a
        except TypeError:
            result += int(a)
    return result
    
def sum_mix(arr):
    return sum(int(x) for x in list(arr))
    
def sum_mix(arr):
    return sum([int(i) for i in arr])
    
def sum_mix(arr): return sum(int(str(d)) for d in arr)
