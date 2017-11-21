# In order to iterate through a list using the index of the list item one can use enumerate.
# Say you wanted to print some upper case letters followed by an index number of lower case letters afterwards:

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# This is another way to achieve the same thing (using title):

def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))
    
# In a more explicit sense this is the same as the following:

def accum(s):
    str = s[0].capitalize()
    for i in range(1, len(s)):
        str += "-" + (s[i] * (i + 1)).capitalize()
    return str
    
# or:

def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]
    
# or:

accum = lambda s: "-".join(((i + 1) * char).capitalize() for i, char in enumerate(s))
