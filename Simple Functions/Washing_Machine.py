# say you wanted to make a washing machine calculator that would return you the amount of water required to wash some clothes if you 
# knew that every extra unit required 10% more water:

def how_much_water(water, clothes, load):
    if load > 2 * clothes:
        return "Too much clothes"

    if load < clothes:
        return "Not enough clothes"

    for i in range(load - clothes):
        water *= 1.1

    return round(water, 2)

# or: 

def how_much_water(l, x, n):
    return "Too much clothes" if n > 2*x else "Not enough clothes" if n < x else round(1.1**(n-x)*l, 2)

# this highlights the importance of making your code easy to understand: I started trying to solve it like so:

def how_much_water(L,X,N):
  if N > 2*X:
    return 'Too much clothes'
  elif N < X:
    return 'Not enough clothes'
  else:
    for i in range(N-X):
      L = L * 1.1
      
  return round(L, 2)

# this was conceptually much harder to understand.
