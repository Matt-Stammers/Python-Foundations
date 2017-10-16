# one way round using multiplication would be to use a for loop. In this case to calculate the cost of some billboard ads with a 
# default argument of 30.

def billboard(name, price=30):
  length = len(name)
  ad_price = 0
  for x in range(length):
    ad_price += price
  return ad_price
  
# even smarter is to us the a different iterator and iterable in a list expression. Python knows to look at the individual components

def billboard(name, price=30):
    return sum(price for letter in name)
    
def billboard(name, price = 30):
    return sum([price for l in name])
    
# or eve this will work:

def billboard(name, price=30):
    return sum(price for _ in name)
