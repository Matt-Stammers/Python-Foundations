# This can be done with a regex:

import re

def shortcut( s ):
    return re.sub('[aeiou]', '', s )
    
# but is probably best done with translate

def shortcut(s):
    return s.translate(None, 'aeiou')
    
# can also done with a list comprehension

def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')
    
# as a lambda function

import re
shortcut = lambda s: re.sub('[aeiou]', '', s)

# using .replace()

def shortcut( s ):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s
    
# or filter

shortcut = lambda s: filter(lambda x: x not in 'aeoui', s)

# there are literally hundreds of options! Python is so amazing ;)
