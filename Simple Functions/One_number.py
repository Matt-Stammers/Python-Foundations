# say you wanted to build a function that would return true if only one individual number is in a string. you could do this:

def isDigit(string):
  split_ = string.split(' ')
  print(split_)
  if len(split_) == 1:
    comb = ''.join(splits for splits in split_)
    print(comb)
    try:
      combs = float(comb)
      print(combs)
      return True
    except:
      return False
  else:
    return False
    
# Regex:

import re
def isDigit(s):
    return re.match(r'^(-?)(([0-9]+\.[0-9]+)|([0-9]+))$',s) is not None
    
import re
def isDigit(string):
    return True if re.search(r'(^-*[0-9\.]+$)',string) else False
    
 def isDigit(string):
    import re
    string = string.strip()
    return bool(re.match("^-?\d*\.{0,1}\d+$",string))
    
# or using is digit:

def isDigit(string):
    return string.lstrip('-').replace('.', '').strip().isdigit()
    
# or:

def isDigit(strng):
    try:
        float(strng)
        return True
    except ValueError:
        return False

