# this is a silly fake binary generator:

def fake_bin(x):
  binary = ''
  for n in x:
    if int(n) < 5:
      binary = binary + '0'
    elif int(n) >= 5:
      binary = binary + '1'
  return binary
  
# the same can be achieved by:

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
    
def fake_bin(x):
    return ''.join(['0' if d < '5' else '1' for d in x])
    
# or possibly even smarter:

import string

def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))
