# If one wanted to double all the values in an array one could use a simple list expression:

def maps(a):
    return [x*2 for x in a]
    
# or as a lambda

maps=lambda a:[n*2 for n in a]

# but one can also use the .map method

def maps(a):
    return list(map(lambda s: s*2, a))
    
def times2(a):
    return a * 2
def maps(a):
    return list(map(times2,a))    
    
def maps(a):
    return list(map(mult,a))
def mult(b):
    return b*2
    
# or .append()  
  
def maps(a):
    res = []
    for x in a:
        res.append (x * 2)
    return res
