# Say you wanted to remove all vowels to the end of a string. You could do it like this:

def move_vowels(input): 
    vows = [ c for c in input if c in 'aeiou' ]
    cons = [ c for c in input if c not in 'aeiou' ]
    return ("".join(cons)+"".join(vows))
    
# or:

def move_vowels(s): 
    result = ''
    vowels = ''
    for c in s:
        if c in 'aeiou':
            vowels += c
        else:
            result += c
    return result + vowels
    
# by using a regex:

import re

def move_vowels(input):
    return ''.join(''.join(l) for l in zip(*re.findall(r'([^aeiou])?([aeiou])?', input)))
    
 # or:
 
 def move_vowels(s): 
    return ''.join(sorted(s, key=lambda k: k in 'aeiou'))
