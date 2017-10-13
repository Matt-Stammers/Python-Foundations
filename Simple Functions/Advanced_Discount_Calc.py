# say we had a situation where we needed to create a discount calculator that scaled, but only up to a certain point. 
# In this case Re: fuel prices. We could do it this way by splitting the two cases using control flow:

def fuel_price(litres, price_per_liter):
  if litres <= 10:
    discount = (litres / 2) * 0.5
    print(litres * price_per_liter - discount)
    return  round(litres * price_per_liter - discount, 2)
  else:
    full_discount = 0.25 * litres
    print(litres * price_per_liter - full_discount)
    return round(litres * price_per_liter - full_discount, 2)
    
# or we could solve it more effectively like so using the min of two arguments:

def fuel_price(litres, price_per_liter):
    discount = int(min(litres, 10)/2) * 5 / 100
    return round((price_per_liter - discount) * litres, 2)
    
# or this:

def fuel_price(litres, price_per_liter):
    final_price = price_per_liter - min((.05 * (litres // 2)), .25)
    
    return round(litres * final_price, 2)
    
# these are perhaps best practice
# but the cleverest solution I have seen is the following using bisect:

from bisect import bisect

def fuel_price(litres, price_per_liter):
    discount = (0, 5, 10, 15, 20, 25)[bisect([2, 4, 6, 8, 10], litres)] * 0.01
    return (litres * price_per_liter) - (litres * discount)

