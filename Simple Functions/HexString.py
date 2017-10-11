# Convert a hexstring to an int easily using python:

def hex_to_dec(s): # all you need to do is put 16 in and python knows exactly what you mean.
    return int(s,16)
    
# you could also do it this way, but it's much more ardous:

def dec(hex):
    h = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'a', 'b', 'c', 'd', 'e', 'f']
    return h.index(hex)

def hex_to_dec(hex):
    result = 0
    hex = list(reversed(hex))
    for idx, c in enumerate(hex):
        result += dec(c) * (16 ** idx)
    return result
    
# or you can:

def hex_to_dec(s):
    return int(eval('0x'+s))
    
# or:

from functools import partial
hex_to_dec = partial(int, base=16)
