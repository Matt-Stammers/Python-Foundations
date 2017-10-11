# what if you wanted to index an item that was nested or not already in a list and return the last item from the array:
# say that x = (1,'b',3','d',5) and you want to return 5
#x[-1] won't work for several items because the function will only accept one.

# Instead you can use *args:

def last(*args):
  return args[-1]
  
# but this won't work either:

# one has to use args[-1][-1]:

def last(*args):
  try:
    return args[-1][-1]
  except:
    return args[-1]

# other options include using collections:

def last(*args):
    import collections
    if len(args) == 1:
        if isinstance(args[0], collections.Iterable):
            return args[0][-1]
        else:
            return args[0]
    else:
        return args[-1]

# or more clearly:

from collections import Iterable

def last(*args):
    return args[-1][-1] if isinstance(args[-1], Iterable) else args[-1]
    
# or even more interesting:

def last(*args):
    return args[-1] if not hasattr(args[-1], "__getitem__") else args[-1][-1]
    
