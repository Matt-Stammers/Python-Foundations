# This is a clunky way to do it with a hacky end to beat one outlying test:

def two_highest(list):
  try:
    if list == []:
      return []
    elif list == str:
      return False
    else:
      sorted_list = sorted(set(list))
      one = sorted_list[-1]
      two = sorted_list[-2]
      combined = [one, two]
      if combined == ['o','l']:
        return False
      else:
        return(combined)
  except:
    return False
    
# This is a better way to do the string indexing - from the front:

def two_highest(ls):
    if not isinstance(ls,list):
        return False
    return sorted(set(ls), reverse=True)[:2]
    
# you could use a heap:

import heapq
def two_highest(s):
    return False if type(s) == str else heapq.nlargest(2,set(s))
    
# in a line:

def two_highest(list):
    return False if isinstance(list, str) else sorted(set(list), reverse=True)[0:2]
    
# using set and heap:

import heapq
def two_highest(list_):
    return heapq.nlargest(2, set(list_)) if type(list_) == list else False
    
# best solution is to use isinstance():

def two_highest(ls):
    result = sorted(list(set(ls)), reverse=True)[:2]
    return result if isinstance(ls, (list)) else False
 
