# Some other ways to return false without actually saying false:

def ifChuckSaysSo():
  return 0
  
ifChuckSaysSo = lambda: 0

def ifChuckSaysSo():
    return True - True
    
a=True
def ifChuckSaysSo():
    # code here
    global a
    a=not a
    return a
    
def ifChuckSaysSo():
    return eval("0") # eval can interpret strings
    
from builtins import int as ifChuckSaysSo

def ifChuckSaysSo():
    this_sucks = True
    return this_sucks - 1
    
# see even programmers have a sense of humour...
