# Say you wanted to calculate the discount on some goods which scales as you buy more. Say 3 for 2 on mangoes:
# you could calculate it like this:

import math

def mango(quantity, price):
  discount_q = math.floor(quantity/3)
  return ((quantity * price) - (discount_q * price))
  
# or using algebra you could rebalance it like this:

def mango(quantity, price):
    return ((quantity/ 3) * (2 * price)) + (quantity % 3 * price)
    
# but the best solution is this:

def mango(quantity, price):
    return (quantity - quantity // 3) * price
