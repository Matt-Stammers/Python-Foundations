# Sum's up all the numbers below a number and returns total ;) Various ways

def summation(num):
    return sum(xrange(num + 1))
    
def summation(num):
    return (1+num) * num / 2
    
def summation(num):
    return sum(range(1,num+1))
    
def summation(num):
    if num > 1:
       return num + summation(num - 1)
    return 1
    
summation = lambda x: sum(range(1, x + 1))

def summation(num):
    sum = 0  # Code here
    while ( num > 0 ):
      sum += num
        num = num - 1
    return sum   
    
def summation(num):
    s = 0
    i = 1
    while i <= num :
        s = s + i
        i = i + 1
    return s
