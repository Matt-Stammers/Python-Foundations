# Various different ways to invert only positive numbers

# using flow control:

def make_negative(number):
    if number >0:
        return number * -1
    elif number <0:
        return number 
    else:
        return 0
        
# using abs:

def make_negative( number ):
    return -abs(number)
    
# 0 - number unless negative
    
def make_negative( number ):
    if number > 0:
        number = 0 - number
    return number
    
# with a lambda

make_negative = lambda num: num * -1 if num >= 0 else num
