# this was my solution to the problem

def distinct(seq):
    l = []
    for i in seq:
        if i not in l:
            l.append(i)
            print(l)
    return l
    
# another option is to use:

def distinct(seq):
    return sorted(set(seq), key = seq.index)
    
# or you can use set() and append()

def distinct(seq):
    result = []
    seen = set()
    for a in seq:
        if a not in seen:
            result.append(a)
            seen.add(a)
    return result

# or you can use a list expression

def distinct(seq):
    nl = []
    [nl.append(i) for i in seq if i not in nl]
    return nl
    
# or with dictionary objects
    
def distinct(seq):
    result = []
    uniques = {i:True for i in set(seq)}
    for object in seq:
        if uniques[object]:
            result.append(object)
            uniques[object] = False
    return result

# or use the ordederedDict function

from collections import OrderedDict
def distinct(seq):
    return list(OrderedDict.fromkeys(seq))
    
from collections import OrderedDict
def distinct(numbers):
    return list(OrderedDict.fromkeys(numbers).keys())

# or a very chunky list expression

def distinct(seq):
    new_seq = []
    [new_seq.append(seq[i]) for i in range(len(seq)) if seq[i] not in new_seq]
    return new_seq
   
# or instead of 'not in' you can use in and continue:

def distinct(seq):
    lst = []
    for i in seq:
        if i in lst:
            continue
        lst.append(i)
    return lst
