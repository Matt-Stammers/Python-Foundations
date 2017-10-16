# say you wanted to select only the inner elements from an array:

import re
def array(string):
  if len(string) <5:
    return None
  else:
    string = re.sub(',',' ',string)
    return string[2:-2] # or 1:-1 would also work here
    
# the formatting can also be done as follows:

def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None
