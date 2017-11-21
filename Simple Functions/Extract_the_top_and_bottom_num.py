# Numbers - high and low

def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
    
# This is much better than the below:

def high_and_low(n):
    a = [a for a in n.split()]
    print(a)
    b = [int(s) for s in a]
    print(b)
    top = max(b)
    bottom = min(b)
    return ''.join(str(top) + ' ' + str(bottom))
    
# or:

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))
  
# or:

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return "{} {}".format(max(n), min(n))
