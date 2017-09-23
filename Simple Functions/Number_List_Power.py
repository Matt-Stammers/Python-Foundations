

def powers_of_two(n):
    result_list = []
    i = 0
    for i in range(n+1):
        result = 2**i
        result_list.append(result)
        i+=1
    return result_list
    
# or a much nicer way to do it:

def powers_of_two(n):
    return [2**x for x in range(n+1)]
    
# powers of two:

def powers_of_two(n):
    a = []
    for i in range(0, n + 1):
        a.append(2 ** i)    
    return a
