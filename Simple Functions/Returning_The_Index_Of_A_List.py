# Returning list indices

def find_needle(haystack):
    return "found the needle at position " + str(haystack.index('needle'))
    
# or without concatenation

def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

# or using .format in Python 3x

def find_needle(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))
    
# or

def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i
