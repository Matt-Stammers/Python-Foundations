# string cleaning - removing one item from the end of the string:

def remove(s):
    return s[:-1] if s.endswith('!') else s
    
def remove(s):
    return s[:-1] if s and s[-1] == '!' else s
    
def remove(s):
    if s.endswith("!"):
        s = s[:-1] 
    return s
    
# probably best to just use a regex though:

def remove(s):
    import re
    return re.sub(r'!$', '', s)

# or

import re
def remove(s):
    return re.sub(r'(!){1}$',"",s)
    
# or

def remove(s):
    if s == '':
        return s
    if s[-1] == '!':
        s = s[0:-1]
    return s
