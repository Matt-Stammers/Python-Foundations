# This will allow one to sort a list using a key (in this case the last letter)

def last(s):
    return sorted(s.split(), key=lambda x: x[-1])
    
# or:

from operator import itemgetter
def last(s):
    return sorted(s.split(), key=itemgetter(-1))
    
# or:

def MyFn(s):
    return s[-1]
def last(s):
    return sorted(s.split(" "), key=MyFn)
    
# or:

def last(s):
    lst = s.split()
    lst.sort(key = lambda x: x[-1])
    return lst
