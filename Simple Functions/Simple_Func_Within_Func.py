# these functions will return one another:

# the best way to do it is with a lambda:

def always(n=0):
    return lambda: n
    
# or

def always(n=0):
    return lambda x=n: x
    
# but you can also do it with a function within:

def always(n=0):
    def result():
        return n
    return result
    
def always(n=0):
  def _func():
    return n
  return _func
 
