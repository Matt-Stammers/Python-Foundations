# the following with check the index and then exponentiate that value in the array:

def index(array, n):
    if n > len(array):
        return -1
    else:
        return array[n]**n
        
def index(array, n):
    try:
        return array[n]**n
    except:
        return -1

def index(array, n):
    return array[n]**n if n <= len(array) - 1 else -1
    
def index(array, n):
    try:
        return pow(array[n],n)
    except IndexError:
        return -1
